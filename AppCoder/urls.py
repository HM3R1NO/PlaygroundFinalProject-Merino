from django.urls import path
from .views import home, about, iniciar_sesion, registrar_cuenta, cerrar_sesion, ver_perfil
from .views import editar_perfil, cambiar_password, ver_chats, iniciar_chat, ver_chat, EliminarChatView
from .views import ver_posts, buscar_posts
from .views import VerPostView, NuevoPostView, EditarPostView, EliminarPostView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),


    path('login/', iniciar_sesion, name='login'),
    path('registro/', registrar_cuenta, name='registrar'),
    path('logout/', cerrar_sesion, name='logout'),
    path('perfil/', ver_perfil, name='ver_perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-password/', cambiar_password, name='cambiar_password'),

    path('chats/', ver_chats, name='ver_chats'),
    path('nuevochat/', iniciar_chat, name='nuevo_chat'),
    path('chat/<int:id>/mensajes/', ver_chat, name='ver_chat'),
    path('chat/<int:pk>/eliminar/', EliminarChatView.as_view(), name='borrar_chat'),

    path('posts/', ver_posts, name='ver_posts'),
    path('buscarpost/', buscar_posts, name='buscar_posts'),
    path('post/<int:pk>', VerPostView.as_view(), name='ver_post'),
    path('nuevopost/', NuevoPostView.as_view(), name='nuevo_post'),
    path('post/<int:pk>/editar/', EditarPostView.as_view(), name='editar_post'),
    path('post/<int:pk>/eliminar/', EliminarPostView.as_view(), name='borrar_post'),
]
