
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contact'),
    path('adm', views.adm, name='adm'),
    path('cat', views.cat, name='cat'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_detail')
]
