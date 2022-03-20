from django import forms

class crearpostform (forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    cuerpo = forms.CharField(max_length=200)
    tags = forms.CharField(max_length=30)


class contactameform(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=200)
    
    
class Usuariosform(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    
    
class buscarpostform(forms.Form):
    tags = forms.CharField(max_length=20)

