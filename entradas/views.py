from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Crearpost,Contactame,Buscarpost,Usuarios
from . forms import crearpostform,contactameform, buscarpostform,Usuariosform

# Create your views here.
def inicio(request):
    return render(request, "index.html",{})



def crearpost(request):
    if request.method == 'POST':
        form= crearpostform(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            post = Crearpost(titulo=data['titulo'], subtitulo=data['subtitulo'], cuerpo=data['cuerpo'],tags=data['tags'])
            post.save()
            return redirect('index')
    form = crearpostform()
    return render(request, "crearposts.html", {'form': form})



def contactame(request):
    if request.method == 'POST':
            form= contactameform(request.POST)
        
            if form.is_valid():
                datacontact = form.cleaned_data
                contacto = Contactame(nombre=datacontact['nombre'],email=datacontact['email'],mensaje=datacontact['mensaje'])
                contacto.save()
            return redirect('index')
    form = contactameform()
    return render(request, "contactame.html", {'form': form})



def buscarpost(request):
    
    buscarportags = request.GET.get('tags', None)
    
    if buscarportags is not None:
        posts = Crearpost.objects.filter(tags__icontains=buscarportags)
    else:
        posts = Crearpost.objects.all()
        
    form = buscarpostform()
    return render(request, "buscarpost.html", {'form': form, 'buscarportags':posts})



def crearusuario(request):
    if request.method == 'POST':
        form= Usuariosform(request.POST)
        
        if form.is_valid():
            datausuario = form.cleaned_data
            usuario = crearusuario(nombre=['nombre'], apellido=data['apellido'], email=data['email'])
            usuario.save()
            return redirect('index')
    form = Usuariosform()
    return render(request, "crearusuario.html", {'form': form})


