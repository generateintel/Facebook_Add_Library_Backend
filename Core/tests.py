from django.db.models import Q
from django.test import TestCase

# Create your tests here.


q=Q()
filter_list=['category','is_active','page_likes__gte','page_likes__lte','followers__gte','followers__lte','active_add__gte','active_add__lte','inactive_add__gte','inactive_add__lte']
for index ,item in enumerate(filter_list, start=0):
    q&=Q(item=="Cate")

print(q)