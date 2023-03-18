from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from .forms import *
from MiRestaurante.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from MiRestaurante.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
def inicio(request):
    mihtml= open("C:/Users/LTA/Desktop/ENTREGAFINAL/restaurante/restaurant/MiRestaurante/templates/MiRestaurante/inicio.html")
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
   
def Entrada1(request):
    if request.user.is_authenticated == True:
        avatar = Avatar.objects.filter(user=request.user.id)
        entrada1 = Entrada.objects.all()
        context = {"Entrada":entrada1, "url":avatar[0].imagen.url}
        return render(request, "MiRestaurante/inicio.html", context)
    else:
        entradas = Entrada.objects.all()
        return render(request, "MiRestaurante/inicio.html", {"Entrada":entradas})

def PlatoP(request):
    if request.user.is_authenticated == True:
        avatar = Avatar.objects.filter(user=request.user.id)
        platoprincipal1 = PlatoPrincipal.objects.all()
        context = {"Plato principal":PlatoP, "url":avatar[0].imagen.url}
        return render(request, "MiRestaurante/inicio.html", context)
    else:
        platoprincipal2 = PlatoPrincipal.objects.all()
        return render(request, "MiRestaurante/inicio.html", {"estadios":platoprincipal2})

def Postres(request):
    if request.user.is_authenticated == True:
        avatar = Avatar.objects.filter(user=request.user.id)
        postres = Postre.objects.all()
        context = {"Postre":postres, "url":avatar[0].imagen.url}
        return render(request, "MiRestaurante/inicio.html", context)
    else:
        postres1 = Postre.objects.all()
        return render(request, "../templates/jugadores.html", {"jugadores":postres1})
    
def entradaFormulario(request):

    if request.method == "POST":
        MiFormulario= EntradaFormulario(request.POST)
        platoimagen= request.FILES.get("txtImagen")
        print(MiFormulario)
        if MiFormulario.is_valid:
            Informacion= MiFormulario.cleaned_data
            restaurante= Entrada (plato= Informacion["Plato"], n_mesa= Informacion ["N_Mesa"])
            restaurante.save()
            return render(request,"MiRestaurante/inicio.html")
        
    else:
        MiFormulario= EntradaFormulario()
    return render (request, "MiRestaurante/Entrada1Formulario.html")

def platoprincipalFormulario(request):

    if request.method == "POST":
        MiFormulario= PlatoPrincipalFormulario(request.POST)
        platoimagen= request.FILES.get("txtImagen")
        print(MiFormulario)
        if MiFormulario.is_valid:
            Informacion= MiFormulario.cleaned_data
            restaurante= PlatoPrincipal (plato= Informacion["Plato"], n_mesa= Informacion ["N_Mesa"])
            restaurante.save()
            return render(request,"MiRestaurante/inicio.html")
        
    else:
        MiFormulario= PlatoPrincipalFormulario()
    return render (request, "MiRestaurante/PlatoPrincipalForm.html")

def postreFormulario(request):

    if request.method == "POST":
        MiFormulario= PostreFormulario(request.POST)
        platoimagen= request.FILES.get("txtImagen")
        print(MiFormulario)
        if MiFormulario.is_valid:
            Informacion= MiFormulario.cleaned_data
            restaurante= Postre(plato= Informacion["Postre"], n_mesa= Informacion ["N_Mesa"])
            restaurante.save()
            return render(request,"MiRestaurante/inicio.html")
        
    else:
        MiFormulario= PostreFormulario()
    return render (request, "MiRestaurante/postreformulario.html")
 
def buscarentrada(request):
    if request.GET["N_mesa"]:
        plato= request.GET["Plato"]
        n_mesa= Entrada.objects.filter(plato__icontains=plato)
        return render(request, "MiRestaurante/BusquedaFormulario.html", {"plato": plato, "n_mesa":n_mesa})

    else:
        respuesta= "No enviaste datos"
    return HttpResponse(respuesta)

def buscarplatoprincipal(request):
    if request.GET["N_mesa"]:
        plato= request.GET["Plato"]
        pedido= PlatoPrincipal.objects.filter(plato__icontains=plato)
        return render(request, "MiRestaurante/BusquedaFormulario.html", {"plato": plato, "n_mesa":pedido})

    else:
        respuesta= "No enviaste datos"
    return HttpResponse(respuesta)

def buscarpostre(request):
    if request.GET["N_mesa"]:
        postre= request.GET["Plato"]
        n_mesa= Postre.objects.filter(plato__icontains=postre)
        return render(request, "MiRestaurante/BusquedaFormulario.html", {"postre": postre, "n_mesa":n_mesa})

    else:
        respuesta= "No enviaste datos"
    return HttpResponse(respuesta)

#def BaseDeDatos(request):
    plato= Entrada.objects.all()
    #avatar = Avatar.objects.filter(user=request.user.id)
    contexto= {"Entrada:":plato}
    return render(request, "MiRestaurante/BaseDeDatos.html", contexto)
    

def eliminardatos(request, datos__nombre):
    plato= Entrada.objects.get(nombre=datos__nombre)
    plato.delete()

    plato= Entrada.objects.all()
    contexto= {"Entrada:":plato}
    return render(request, "MiRestaurante/Entrada1Formulario.html", contexto)

def eliminardatos(request, datos__nombre):
    plato= PlatoPrincipal.objects.get(nombre=datos__nombre)
    plato.delete()

    plato= PlatoPrincipal.objects.all()
    contexto= {"Entrada:":plato}
    return render(request, "MiRestaurante/PlatoPrincipalForm.html", contexto)

def eliminardatos(request, datos__nombre):
    plato= Postre.objects.get(nombre=datos__nombre)
    plato.delete()

    plato= Postre.objects.all()
    contexto= {"Entrada:":plato}
    return render(request, "MiRestaurante/postreformulario.html", contexto)

def editardatos(request, plato_nombre):
    plato=Entrada.objects.all()
    if request.method == "POST":
        miFormulario= EntradaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            Informacion= miFormulario.cleaned_data
            plato.plato= Informacion["Plato"]
            plato.cantidad= Informacion["Cantidad"]
            plato.bebida= Informacion["Bebida"]
            plato.numero_de_mesa= Informacion["Numero de mesa"]
            plato.save()
            return render(request, "MiRestaurante/inicio.html")
        
        else:
            miFormulario= EntradaFormulario(initial={"Plato": plato.plato, "Cantidad": plato.cantidad, "Bebida": plato.bebida, "Numero de mesa": plato.numero_de_mesa})
        return render(request, "MiRestaurante/BusquedaFormulario.html", {"MiFormulario": miFormulario})

def editardatos(request, plato_nombre):
    plato=PlatoPrincipal.objects.all()
    if request.method == "POST":
        miFormulario= PlatoPrincipalFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            Informacion= miFormulario.cleaned_data
            plato.plato= Informacion["Plato"]
            plato.cantidad= Informacion["Cantidad"]
            plato.bebida= Informacion["Bebida"]
            plato.numero_de_mesa= Informacion["Numero de mesa"]
            plato.save()
            return render(request, "MiRestaurante/inicio.html")
        
        else:
            miFormulario= PlatoPrincipalFormulario(initial={"Plato": plato.plato, "Cantidad": plato.cantidad, "Bebida": plato.bebida, "Numero de mesa": plato.numero_de_mesa})
        return render(request, "MiRestaurante/BusquedaFormulario.html", {"MiFormulario": miFormulario})
    
def editardatos(request, plato_nombre):
    plato=Postre.objects.all()
    if request.method == "POST":
        miFormulario= PostreFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            Informacion= miFormulario.cleaned_data
            plato.postre= Informacion["Postre"]
            plato.cantidad= Informacion["Cantidad"]
            plato.numero_de_mesa= Informacion["Numero de mesa"]
            plato.save()
            return render(request, "MiRestaurante/inicio.html")
        
        else:
            miFormulario= PostreFormulario(initial={"Postre": plato.postre, "Cantidad": plato.cantidad, "Numero de mesa": plato.numero_de_mesa})
        return render(request, "MiRestaurante/BusquedaFormulario.html", {"MiFormulario": miFormulario})    

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
       if form.is_valid():
            usuario= form.cleaned_data.get("username")
            contraseña= form.cleaned_data.get("Password")
            user= authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request,"MiRestaurante/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
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

    return render(request,"MiRestaurante/registro.html", {"form": form} )

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



#def inicio(request):
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