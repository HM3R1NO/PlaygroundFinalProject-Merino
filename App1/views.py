from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import *
from django.urls import reverse_lazy

class App1ListView(View):
    def get(self,request,*args, **kwargs):
        posts=Post.objects.all() #se llaman a todos los objetos del modelo


        context={
            'posts':posts #primero va el nombre al cual se hace referencia en el html y luego la variable que contiene la info.
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
    
class App1DetailView(View):
    def get(self,request,pk, *args,**kwargs): #esta vez incluimos el pk(id) especifica y unica de la instancia creada para hacer uso de el.
        post= get_object_or_404(Post, pk=pk)# de esta forma pedimos el pk correspondiente a la instancia.
        context={
            'post':post
        }
        return render(request, 'app1_detail.html', context)

class App1UpdateView(UpdateView):
    model=Post #se le pasa el modelo que vamos a editar.
    fields=['title','content']
    template_name='app1_update.html'

    def get_success_url(self): #esta parte del codigo recupera el pk para utilizarlo en la url detail
        pk=self.kwargs['pk'] 
        return reverse_lazy("App1:detail", kwargs={'pk':pk})

class App1DeleteView(DeleteView):
    model=Post
    template_name='app1_delete.html'
    success_url= reverse_lazy('App1:home')
