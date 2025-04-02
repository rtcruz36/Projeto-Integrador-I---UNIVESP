from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_medicamento, name='cadastrar_medicamento'),
    path('editar/<int:id>/', views.editar_medicamento, name='editar'),
    path('saida/', views.registrar_saida, name='registrar_saida'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('', views.lista_medicamentos, name='lista_de_medicamentos'),
    path('editar/<int:id>/', views.editar_medicamento, name='editar'),


]

#from django.urls import path
#from . import views

#urlpatterns = [
    # outras rotas...
    #path('accounts/profile/', views.profile, name='profile'),
#]


