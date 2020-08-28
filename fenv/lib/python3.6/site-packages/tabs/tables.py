"""Table base classes for defning new tables"""
import inspect
from abc import ABCMeta, abstractmethod
import hashlib
import dill as pickle
import pandas as pd

def post_process(table, post_processors):
    """Applies the list of post processing methods if any"""
    table_result = table
    for processor in post_processors:
        table_result = processor(table_result)
    return table_result

def describe(cls, full=False):
    """Prints a description of the table based on the provided
    documentation and post processors"""
    divider_double = "=" * 80
    divider_single = "-" * 80
    description = cls.__doc__
    message = []
    message.append(divider_double)
    message.append(cls.__name__ + ':')
    message.append(description)
    if full and cls.post_processors(cls):
        message.append(divider_single)
        message.append("Post processors:")
        message.append(divider_single)
        for processor in cls.post_processors(cls):
            message.append(">" + " " * 3 + processor.__name__ + ':')
            message.append(" " * 4 + processor.__doc__)
            message.append('')
    message.append(divider_double)
    message.append('')
    for line in message:
        print(line)


class BaseTableABC(metaclass=ABCMeta):
    """Abstract Base class for minimum table import"""

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @abstractmethod
    def source(self):
        """Path to the original raw data"""
        pass
    source.dependencies = list()

    @abstractmethod
    def output(self):
        """Path to the processed table (output path)"""
        pass

    @abstractmethod
    def fetch(self, rebuild=False, cache=True):
        """Method for fetching data"""
        pass

    @abstractmethod
    def post_processors(self):
        """A list of functions to be applied for post processing"""
        return list()

    @classmethod
    def describe_processors(cls):
        """List all postprocessors and their description"""
        # TODO: Add dependencies to this dictionary
        for processor in cls.post_processors(cls):
            yield {'name': processor.__name__,
                   'description': processor.__doc__,
                   'processor': processor}

    @classmethod
    def describe(cls, full=False):
        """Prints a description of the table based on the provided
            documentation and post processors.

        Args:
            full (bool): Include post processors in the printed description.
        """
        return describe(cls, full)

    @classmethod
    def dependencies(cls):
        """Returns a list of all dependent tables,
        in the order they are defined.

        Add new dependencies for source and every post proecssor like this::

            source.dependencies = [PersonalData]
            some_post_processor.dependencies = [SomeOtherTable, AnotherTable]

        `some_post_processor.dependencies` needs to be placed after
        `some_post_processor` is defined.
        """
        dependencies = []
        try:
            dependencies += cls.source.dependencies
        except AttributeError:
            pass
        for processor in cls.post_processors(cls):
            try:
                assert isinstance(processor.dependencies, list), \
                    "{}.dependencies must be a list".format(processor.__name__)
                dependencies += processor.dependencies
            except AttributeError:
                pass
        return dependencies

    dep = dependencies
    """dep is an alias of dependencies"""
    # TODO: Make dependent columns method for use in tests.

    def get_settings_list(self):
        """The settings list used for building the cache id."""
        return [
            self.source,
            self.output,
            self.kwargs,
            self.post_processors,
        ]

    def get_hash(self):
        """Retruns a hash based on the the current table code and kwargs.
        Also changes based on dependent tables."""
        depencency_hashes = [dep.get_hash() for dep in self.dep()]
        sl = inspect.getsourcelines
        hash_sources = [sl(self.__class__), self.args,
                        self.kwargs, *depencency_hashes]
        hash_input = pickle.dumps(hash_sources)
        return hashlib.md5(hash_input).hexdigest()

    def get_cached_filename(self, filename, extention, settings_list=None):
        """Creates a filename with md5 cache string based on settings list

        Args:
            filename (str): the filename without extention
            extention (str): the file extention without dot. (i.e. 'pkl')
            settings_list (dict|list): the settings list as list (optional)
                NB! The dictionaries have to be sorted or hash id will change
                arbitrarely.
        """
        cached_name = "_".join([filename, self.get_hash()])
        return ".".join([cached_name, extention])

class Table(BaseTableABC, metaclass=ABCMeta):
    """MetaClass for defining tables.

    Attention! The following methods are required when defining a
    class the inherits from Table

    Methods:
        source(self): Should return the table.
            For example pd.read_csv() **(required, method)**

        output(self): Should return the output path for
            where the finished table should be stored.
            For example a cache directory. **(required, method)**

        post_processors(self): a list of post processor
            functions of methods. **(required, method)**

    Example:
        Defining a table::

            class UserDataTable(Table):
                def source(self):
                    return pd.read_csv('/path/to/file')

                def output(self):
                    return "/path/to/output"

                def post_processors(self):
                    return [
                        my_custom_function(),
                        my_second_custom_function(),
                    ]

    """

    def __init__(self, *args, **kwargs):
        super(Table, self).__init__(*args, **kwargs)

    @abstractmethod
    def source(self):
        """Path to the original raw data"""
        pass

    @abstractmethod
    def output(self):
        """Path to the processed table (output path)"""
        pass

    @abstractmethod
    def post_processors(self):
        """A list of functions to be applied for post processing"""
        return list()

    def to_cache(self, table):
        """Defines the default cache method. Can be overwritten if needed"""
        table.to_pickle(self.output())

    def read_cache(self):
        """Defines how to read table from cache.
        Should be overwritten if to cache is overwritten"""
        return pd.read_pickle(self.output())

    def _process_table(self, cache=True):
        """Applies the post processors"""
        table = self.source()
        assert not isinstance(table, None.__class__), \
            "{}.source needs to return something, not None".format(self.__class__.__name__)
        table = post_process(table, self.post_processors())
        if cache:
            self.to_cache(table)
        return table

    # TODO: Check upstream if a table needs to be rerun (will be fixed based on hash included in settings for dependent variables)

    def fetch(self, rebuild=False, cache=True):
        """Fetches the table and applies all post processors.
        Args:
            rebuild (bool): Rebuild the table and ignore cache. Default: False
            cache (bool): Cache the finished table for faster future loading.
                Default: True
        """
        if rebuild:
            return self._process_table(cache)
        try:
            return self.read_cache()
        except FileNotFoundError:
            return self._process_table(cache)
