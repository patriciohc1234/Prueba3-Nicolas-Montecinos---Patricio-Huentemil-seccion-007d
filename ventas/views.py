from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Catalogo
from django.views import generic
from .forms import CrearForm
from django.urls import reverse_lazy
#crear funcion del numero de catalogos creados
def index(request):
 
    num_catalogo=Catalogo.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_catalogo':num_catalogo},
    )


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#Listar los productos
class CatalogoListView(generic.ListView):
    model = Catalogo
    

class CatalogoDetailView(generic.DetailView):
    model = Catalogo

#crear un producto con un form
def crearproducto(request):
	if request.method =='POST':
		form = CrearForm(request.POST)
		if form.is_valid():
			form.save()
		return render(request,'ventas/hecho.html')
	else:
		form = CrearForm()

		return render(request,'ventas/crear.html',{'form':form})
#pagina de confirmacion de la creacion
def hecho(request):
    return render(request,'ventas/hecho.html')
#editar el producto
def editarproducto(request):
    if request.method == "POST":
        form = CrearForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
    else:
        form = CrearForm()
    return render(request, 'ventas/editar.html', {'form': form})
#eliminar el producto no compilado
def eliminar(request, catalogo_id):
    instancia = Catalogo.objects.get(id=catalogo_id)
    instancia.delete()
    return redirect('/catalogo_list')

