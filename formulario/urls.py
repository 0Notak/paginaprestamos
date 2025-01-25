from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('', views.formulario_vista, name='registro_formulario'),
   path('lista/', views.lista_formularios, name='lista_formularios'),
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
   path('blog/', views.blog, name='blog'),
    
    path('blog/<slug:slug>/', views.preview, name='preview'),
   
]