"""Tables module"""
import sys
import pkgutil
import importlib
from inspect import getmembers, isclass, isabstract
from tabs.tables import Table

def get_all_modules(package_path):
    """Load all modules in a package"""
    return [name for _, name, _ in pkgutil.iter_modules([package_path])]

def get_all_classes(module_name):
    """Load all non-abstract classes from package"""
    module = importlib.import_module(module_name)
    return getmembers(module, lambda m: isclass(m) and not isabstract(m))


class Tabs():
    """Class for loading a list of all defined tables,
    similar to tabs in a browser.

    Args:
        package_path (str): Path to package containing defined tables
        custom_table_classes (list(class)): A list of custom Table metaclasses
            that should also be recognised and added to the tabs list.

    Example:
        Using tabs for listing tables::

            from tabs import Tabs
            package_path = os.path.dirname(os.path.realpath(__file__))
            tabs = Tabs(package_path)
            tabs.table_list()

            > Avaiable tables:
            > Persondata
            > OtherData


        Fetching a defined table::

            person_data = tabs('Persondata').fetch()
    """

    def __init__(self, package_path=None, custom_table_classes=None):
        self.tabs = {}
        self._update_sys_path(package_path)
        self.find_tabs(custom_table_classes=custom_table_classes or list())

    def __iter__(self):
        for item in self.tabs:
            yield item

    def __call__(self, table_name, **kwargs):
        """Calling the class directly with a table_name returns
        that table object"""
        return self.load(table_name, **kwargs)

    def __repr__(self):
        table_names = ", ".join(
            [table_name for table_name, _ in self.tabs.items()]
        )
        return "Tables ({})".format(table_names)

    def load(self, table_name, **kwargs):
        """Get table object by name, initialized and ready.
        Same as using __call__"""
        return self.get(table_name)(**kwargs)

    def get(self, table_name):
        """Load table class by name, class not yet initialized"""
        assert table_name in self.tabs, \
            "Table not avaiable. Avaiable tables: {}".format(
                ", ".join(self.tabs.keys())
            )
        return self.tabs[table_name]

    def _update_sys_path(self, package_path=None):
        """Updates and adds current directory to sys path"""
        self.package_path = package_path
        if not self.package_path in sys.path:
            sys.path.append(self.package_path)

    def table_list(self):
        """Display the table names"""
        for table_name, _ in self.tabs.items():
            print(table_name)

    def find_tabs(self, custom_table_classes=None):
        """Finds all classes that are subcalss of Table and loads them into
         a dictionary named tables."""
        for module_name in get_all_modules(self.package_path):
            for name, _type in get_all_classes(module_name):
                # pylint: disable=W0640
                subclasses = [Table] + (custom_table_classes or list())
                iss_subclass = map(lambda c: issubclass(_type, c), subclasses)
                if isclass(_type) and any(iss_subclass):
                    self.tabs.update([[name, _type]])

    def describe_all(self, full=False):
        """Prints description information about all tables registered
        Args:
            full (bool): Also prints description of post processors.
        """
        for table in self.tabs:
            yield self.tabs[table]().describe(full)
