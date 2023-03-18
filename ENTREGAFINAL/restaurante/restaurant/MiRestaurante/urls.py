from django.urls import path, include
from MiRestaurante import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio),
    path("gastronomia", views.gastronomia, name="Gastronomia"),
    path("informacion", views.informacion, name="Informacion"),
    path("contacto", views.contacto, name="Contacto"),
    path("inicio", views.inicio, name="Inicio"),
    path("platoprincipalformulario", views.platoprincipalFormulario, name="platoprincipalFormulario"),
    path("entradaformulario", views.entradaFormulario, name="EntradaFormulario"),
    path("postreformulario", views.postreFormulario, name="postreFormulario"),
    path("Entrada", views.Entrada1, name="Entrada"),
    path("PlatoPrincipal", views.PlatoP, name="Plato Principal"),
    path("Postres", views.Postres, name="Postres"),
    path("acercademi", views.acercademi, name="acercademi"),
    path("busquedaformulario", views.buscarplatoprincipal, name="busquedaformulario"),
    path("busquedaformulario", views.buscarpostre, name="busquedaformulario"),
    path("eliminardatos", views.eliminardatos, name="EliminarDatos"),
    path("editardatos", views.editardatos, name="editardatos"),
    path("busquedaformulario", views.buscarentrada, name="busquedaformulario"),
    path("plato/list", views.PlatoList.as_view(), name="list"),
    path('platodetalle', views.PlatoDetalle.as_view(), name="Detail"),
    path('platocreacion', views.PlatoCreacion.as_view(), name="New"),
    path('platoupdate', views.PlatoUpdate.as_view(), name="Edit"),
    path('platodelete', views.PlatoDelete.as_view(), name="Delete"),
    path("login", views.login_request, name="login"),
    path("registro", views.registro, name="registro"),
    path("logout", LogoutView.as_view(template_name= "MiRestaurante/logout.html"), name="Logout"),
    path("editarperfil", views.editarperfil, name="editarperfil"),
    #path("agregarAvatar", views.agregarAvatar, name="AgregarAvatar"),
]