from django.shortcuts import render, redirect 
from django.views.generic import View
from .forms import PostCreateForm
from .models import *

class App1ListView(View):
    def get(self,request,*args, **kwargs):
        context={

    }
        return render(request, 'app1_list.html', context)
    
    pass

class App1CreateView(View):
    def get(self, request, *args,**kwargs):
        form=PostCreateForm()  
        context={
            'form':form
        }
        return render(request, 'app1_create.html', context)
    
    #Metodo que permite crear solo una instancia. sin repetir los mismos datos. (por ejemplo en caso de usuarios, solo un usuario con los mismos datos)
    def post(self, request, *args,**kwargs):
        if request.method=='POST':
            form=PostCreateForm(request.POST) #De esta forma se le pasa al Formulario->modelo la información agregada por el usuario. (request.POST)
            if form.is_valid():
                title=form.cleaned_data.get('title') #Guardamos en la variable title la información limpiada, y obtenida (get) del campo 'title' del Form.
                content=form.cleaned_data.get('content')
                p,created=Post.objects.get_or_create(title=title, content=content)#esta función devolverá la instancia del modelo Post si esta ya fue creada o la creara en caso contrario 
                #primera variable title hace referencia al modelo
                #la segunda variable title hace referencia a la variable guardada desde el formulario
                #mismo caso para la variable content.
                #created sera una variable resultante de la descomposicion de la función get_or_create().
                #created sera False si se encontro una instancia ya creada, y True si la instncia se creo por primera vez.
            p.save()
            return redirect('App1:home')
            
        context={
            
        }
        return render(request, 'app1_create.html', context)

