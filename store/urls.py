from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('catrgory/<slug:category_slug>/', views.store, name='products_by_category'),
    path('catrgory/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product detail'),
    path('search/', views.search, name='search'),
]
