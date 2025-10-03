from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_productos, name="home"),
    path('productos/', views.lista_productos, name="Productos"),
    path('inventario/', include('inventario.urls')),
]
