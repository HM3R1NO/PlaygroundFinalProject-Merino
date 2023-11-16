from django.shortcuts import render
from django.views.generic import View

class App1ListView(View):
    def get(self,request,*args, **kwargs):
        context={

    }
        return render(request, 'app_list.html', context)
    
    pass
