from django.urls import path
from . import views
from .views import home_view
# from .views import ProductListView, CreateProductView, ProductDetailView, ProductUpdateView, ProductDeleteView, \
#     CategoryCreateView, HomeView, CategoryDetailView, CategoryListView, SearchView

# from .views import *
urlpatterns = [
    path('', views.home_view, name='home'),
    # path('product_list/', ProductListView.as_view(), name='product_list'),
]
