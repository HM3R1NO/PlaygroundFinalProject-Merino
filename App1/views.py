from django.shortcuts import render
from django.views.generic import View
from .forms import PostCreateForm

class App1ListView(View):
    def get(self,request,*args, **kwargs):
        context={

    }
        return render(request, 'app1_list.html', context)
    
    pass

class App1CreateView(View):
    def get(self, request, *args,**kwargs):
        context={

        }
        return render(request, 'app1_create.html', context)
    
    def post(self, request, *args,**kwargs):
        context={
            
        }
        return render(request, 'app1_create.html', context)

