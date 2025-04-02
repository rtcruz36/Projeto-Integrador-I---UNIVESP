from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_medicamento, name='cadastrar'),
    path('editar/<int:id>/', views.editar_medicamento, name='editar'),
    path('saida/', views.registrar_saida, name='registrar_saida'),
    path('registro/', views.registrar_usuario, name='registro'),

]


