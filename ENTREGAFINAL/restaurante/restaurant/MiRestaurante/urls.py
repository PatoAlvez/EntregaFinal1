from django.urls import path, include
from MiRestaurante import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio),
    path("gastronomia", views.gastronomia, name="Gastronomia"),
    path("informacion", views.informacion, name="Informacion"),
    path("contacto", views.contacto, name="Contacto"),
    path("inicio", views.inicio, name="Inicio"),
    path("RestauranteFormulario", views.RestauranteFormulario, name="RestauranteFormulario"),
    path("entradaformulario", views.entradaFormulario, name="EntradaFormulario"),
    path("acercademi", views.acercademi, name="AcercaDeMi"),
    path("BaseDeDatos", views.BaseDeDatos, name="BaseDeDatos"),
    path("busquedaformulario", views.busquedaFormulario, name="BusquedaFormulario"),
    path("eliminardatos", views.eliminardatos, name="EliminarDatos"),
    path("buscar", views.buscar, name="Buscar"),
    path("plato/list", views.PlatoList.as_view(), name="list"),
    path('platodetalle', views.PlatoDetalle.as_view(), name="Detail"),
    path('platocreacion', views.PlatoCreacion.as_view(), name="New"),
    path('platoupdate', views.PlatoUpdate.as_view(), name="Edit"),
    path('platodelete', views.PlatoDelete.as_view(), name="Delete"),
    path("login", views.login_request, name="login"),
    path("register", views.registro, name="Registro"),
    path("logout", LogoutView.as_view(template_name= "MiRestaurante/logout.html"), name="Logout"),
    path("editarperfil", views.editarperfil, name="editarperfil"),
    #path("agregarAvatar", views.agregarAvatar, name="AgregarAvatar"),
]