from django.urls import path
from . import views

urlpatterns = [
    # URLs principales con nombres estándar
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/nuevo/', views.producto_create, name='producto_create'),
    path('productos/<int:pk>/', views.producto_detail, name='producto_detail'),
    path('productos/<int:pk>/editar/', views.producto_update, name='producto_update'),
    path('productos/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),
    path('clientes/nuevo/', views.cliente_create, name='cliente_create'),
    path('ventas/nueva/', views.venta_create, name='venta_create'),
]