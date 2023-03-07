from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .forms import *
from MiRestaurante.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RestauranteFormulario, UserRegisterForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
@login_required
def inicio(request):
    mihtml= open("C:/Users/LTA/Desktop/ENTREGA3/restaurante/restaurant/MiRestaurante/templates/MiRestaurante/inicio.html")
    plantilla= Template(mihtml.read())
    mihtml.close()
    miContexto= Context()
    documento= plantilla.render(miContexto)
    return HttpResponse(documento)
    
def gastronomia(request):
    return render(request, "MiRestaurante/gastronomia.html")
    

def informacion(request):
    return render(request, "MiRestaurante/informacion.html")
    
def contacto(request):
    return render(request, "MiRestaurante/contacto.html")

def acercademi(request):
    return render(request, "MiRestaurante/acercademi.html") 
   
def restauranteFormulario(request):

    if request.method == "POST":
        MiFormulario= RestauranteFormulario(request.POST)
        print(MiFormulario)
        if MiFormulario.is_valid:
            Informacion= MiFormulario.cleaned_data
            restaurante= Entrada (plato= Informacion["Plato"], n_mesa= Informacion ["N_Mesa"])
            restaurante.save()
            return render(request,"MiRestaurante/inicio.html")
        
    else:
        MiFormulario= RestauranteFormulario()
    return render (request, "MiRestaurante/RestauranteFormulario.html")

def entradaFormulario(request):
    if request.method == "POST":
        MiFormulario= EntradaFormulario(request.POST)
        print(MiFormulario)
        if MiFormulario.is_valid:
            Informacion= MiFormulario.cleaned_data
            restaurante= Entrada (plato= Informacion["Plato"], n_mesa= Informacion ["N_Mesa"])
            restaurante.save()
            return render(request,"MiRestaurante/inicio.html")
        
    else:
        MiFormulario= EntradaFormulario()
    return render(request, "MiRestaurante/RestauranteFormulario.html",{"MiFormulario": MiFormulario})

def busquedaFormulario(request):
    return render (request,"MiRestaurante/busquedaFormulario.html")

def buscar(request):
    if request.GET["N_mesa"]:
        plato= request.GET["Plato"]
        n_mesa= PlatoPrincipal.objects.filter(plato__icontains=plato)
        return render(request, "MiRestaurante/resultadosbusqueda.html", {"plato": plato, "n_mesa":n_mesa})

    else:
        respuesta= "No enviaste datos"
    return HttpResponse(respuesta)

def BaseDeDatos(request):
    plato= Entrada.objects.all()
    contexto= {"Entrada:":plato}
    return render(request, "MiRestaurante/BaseDeDatos.html", contexto)
    

def eliminardatos(request, datos__nombre):
    plato= Entrada.objects.get(nombre=datos__nombre)
    plato.delete()

    plato= Entrada.objects.all()
    contexto= {"Entrada:":plato}
    return render(request, "MiRestaurante/BaseDeDatos.html", contexto)

class PlatoList(ListView):
    model= Entrada
    template_name="MiRestaurante/plato_list.html"

class PlatoDetalle(DetailView):
    model= Entrada
    template_name= "MiRestaurante/plato_detalle.html"

class PlatoCreacion(CreateView):
    model=Entrada
    success_url="/MiRestaurante/plato/list"
    fields=["Plato","Numero de Mesa"]

class PlatoUpdate(UpdateView):
    model=Entrada
    success_url="/MiRestaurante/plato/list"
    fields=["Plato","Numero de Mesa"]

class PlatoDelete(DeleteView):
    model=Entrada
    success_url="/MiRestaurante/plato/list"

def login_request(request):
    if request.method == "POST":
       form= AuthenticationForm(request, data= request.POST)
       if form.is_valid:
            usuario= form.cleaned_data.get("Username")
            contraseña= form.cleaned_data.get("Password")
            user= authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request,"MiRestaurante/inicio.html", {"Mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"MiRestaurante/inicio.html", {"Mensaje":"Error, datos incorrectos"})
    else:
        return render(request,"MiRestaurante/inicio.html", {"Mensaje":"Error"})
    
    form= AuthenticationForm()
    return render(request,"MiRestaurante/login.html", {"form": form} )

def registro(request):
    if request.method == "Post":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data ["Username"]
            form.save()
            return render(request, "MiRestaurante/inicio.html", {"mensaje":"Usuario creado"})
    else:
        form= UserRegisterForm()

    return render(request,"MiRestaurante/login.html", {"form": form} )

def editarperfil(request):
    usuario=request.user
    if request.method == "POST":
        miFormulario= UserEditForm(request.POST)
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            usuario.email= informacion ["email"]
            usuario.password1= informacion["password1"]
            usuario.password2= informacion["password2"]
            usuario.save()

            return render(request, "MiRestaurante/inicio.html")
    else:
        miFormulario= UserEditForm(initial={"email": usuario.email})

    return render(request, "MiRestaurante/editarperfil.html", {"MiFormulario": miFormulario, "Usuario": usuario})

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'MiRestaurante/cambiocontraseña.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'MiRestaurante/cambiocontraseñaexitoso.html', {})



def inicio(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    return render(request, "MiRestaurante/inicio.html", {"url": avatares[0].imagen.url})

#def agregarAvatar(request):
    if request.method == "POST":
        miFormulario= AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid:
            u= User.objects.get (username=request.user)
            avatar= Avatar (user=u, imagen=miFormulario.cleaned.data["imagen"])
            avatar.save()
            return render("MiRestaurante/inicio.html")
    else:
        miFormulario= AvatarFormulario()
    return render(request, "MiRestaurante/agregarAvatar.html", {"MiFormulario": miFormulario})


#class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)