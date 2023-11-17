from django import forms 
from .models import Post 

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post #hace referencia al modelo Post de .models. 
                    #Por lo que los datos ingresados en el formulario darán a lugar a un objeto de esta clase (Post). 
        fields=('title', 'content')