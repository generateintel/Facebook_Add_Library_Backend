from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class Pagination:
  def __init__(self,request, model_name, orderby_lookup,number_of_instance,model_serializer):
    self.request=request
    self.model_name = model_name
    self.orderby_lookup = orderby_lookup
    self.number_of_instance=number_of_instance
    self.model_serializer=model_serializer
  def split_instances_into_pagination(self):
      all_pages = self.model_name.objects.filter(is_active=True).order_by('-'+self.orderby_lookup)
      paginator = Paginator(all_pages, self.number_of_instance)
      page = self.request.GET.get('page')
      try:
          data = paginator.page(page)
      except PageNotAnInteger:

          data = paginator.page(1)
      except EmptyPage:

          data = paginator.page(paginator.num_pages)

      serializer_context = {'request': self.request}
      serializer = self.model_serializer(data, many=True, context=serializer_context)
      # serializer = InfluencerSerializer(data, many=True, context=serializer_context)
      items = paginator.count
      pages = paginator.num_pages
      res = {
          'totalItems': items,
          'totalPages': pages,
          'results': serializer.data
      }

      return res

class Filter_Pagination:
  def __init__(self,request,filter_data, orderby_lookup,number_of_instance,model_serializer):
    self.request = request
    self.filter_data = filter_data
    self.orderby_lookup = orderby_lookup
    self.number_of_instance=number_of_instance
    self.model_serializer=model_serializer
  def split_instances_into_pagination(self):
      paginator = Paginator(self.filter_data, self.number_of_instance)
      page = self.request.GET.get('page')
      try:
          data = paginator.page(page)
      except PageNotAnInteger:

          data = paginator.page(1)
      except EmptyPage:

          data = paginator.page(paginator.num_pages)

      serializer_context = {'request': self.request}
      serializer = self.model_serializer(data, many=True, context=serializer_context)
      # serializer = InfluencerSerializer(data, many=True, context=serializer_context)
      items = paginator.count
      pages = paginator.num_pages
      res = {
          'totalItems': items,
          'totalPages': pages,
          'results': serializer.data
      }

      return res