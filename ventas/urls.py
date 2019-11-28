from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('catalogo/', views.CatalogoListView.as_view(), name='catalogo'),
    path('crear/',views.crearproducto,name='crear'),
    path('hecho/',views.hecho,name='hecho'),
    path('editar/', views.editarproducto, name='editar'),
    path('catalogo/<int:catalogo_id>', views.eliminar, name='catalogo-delete'),
]