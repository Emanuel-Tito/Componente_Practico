from django.urls import path
from core import views

app_name = 'core'  # define un espacio de nombre para la aplicacion
urlpatterns = [
    # path('', views.home,name='home'),
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('supplier_list/', views.SupplierListView.as_view(), name='supplier_list'),
    path('supplier_create/', views.SupplierCreateView.as_view(),name='supplier_create'),
    path('supplier_update/<int:pk>/',views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier_detail/<int:pk>/',views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier_delete/<int:pk>/',views.SupplierDeleteView.as_view(), name='supplier_delete'),
    # Login
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signin/', views.SigninView.as_view(), name='signin'),
    path('signout/', views.SignoutView.as_view(), name='signout'),

    # Producto
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/',views.ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/',views.ProductDeleteView.as_view(), name='product_delete'),
]
