from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from usuarios.form import PerfilForm
from usuarios.models import Perfil



def home(request):
    form = AuthenticationForm()
    formulario = UserCreationForm()
    return render_to_response('inicio.html',{'form':form,'formulario':formulario}, context_instance=RequestContext(request))


def index(request):
   
    return render_to_response('home.html',{
       
    }, context_instance=RequestContext(request))


def new_users(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('usuarios/new_user.html', {
        'formulario':formulario,
        }, context_instance=RequestContext(request))

def loged_in(request):
    if not request.user.is_anonymous():
        return  HttpResponseRedirect('usuarios/perfil')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request.POST)
            if form.is_valid:
                usuario = request.POST['username']
                clave = request.POST['password']
                existe = authenticate(username = usuario, password = clave)
                if existe is not None:
                    if existe.is_active:
                        login(request, existe)
                        messages.add_message(request, messages.INFO, "Inicio de Sesion Exitoso")
                        messages.add_message(request, messages.INFO, "Complete su Perfil")
                        return HttpResponseRedirect('/perfil')
                    else:
                        messages.add_message(request, messages.INFO, "Su Cuenta NO esta ACTIVADA <strong>CONTACTESE CON EL ADMONISTRADOR</strong>")
                        return HttpResponseRedirect('/')
                else:
                    messages.add_message(request, messages.INFO, "USTED NO ESTA REGISTRADO")
                    return HttpResponseRedirect('/user/nuevo')
        else:
            form = AuthenticationForm()
        return render_to_response('usuarios/iniciar_sesion.html',{
            'form':form,
        }, context_instance=RequestContext(request))

@login_required(login_url='/login')
def loged_out(request):
    logout(request)
    #messages.add_message(request, messages.INFO, "Cuenta cerrada correctamente")
    return HttpResponseRedirect('/')


@login_required(login_url = '/login')
def perfil(request):
    if request.user.is_authenticated():
        usuario=request.user
        context = {
        'usuario'  : usuario,
        'nombre' : usuario.get_full_name(),
        
       
        }
        return render_to_response("usuarios/perfil.html",context,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/login/")
        

@login_required(login_url = '/login')
def new_perfil(request):
    if request.method == 'POST':
        formulario = PerfilForm(request.POST, request.FILES)
        if formulario.is_valid():
            perfil = formulario.save()
            perfil.usuario = request.user
            perfil.save()
            return HttpResponseRedirect('/perfil')
    else:
        formulario = PerfilForm()
    return render_to_response('perfil/new_perfil.html',{
        'formulario':formulario,
    }, context_instance=RequestContext(request))


def producto(request):
       return render_to_response('nuevoproducto.html',{
        
    }, context_instance=RequestContext(request))


    