from django.shortcuts import render
from .forms import ReservaForm

# Create your views here.
def index(request):
    return render(request, 'taller/Index.html', {})

def login(request):
    return render(request, 'taller/Login.html', {})

def agendar(request):
    data = {
        'form': ReservaForm()
    }
    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Reserva realizada!"
        else:
            data["form"] = formulario
            
    return render(request, 'taller/Agendar.html', data)

def trabajos(request):
    return render(request, 'taller/Trabajos.html', {})

def nosotros(request):
    return render(request, 'taller/Nosotros.html', {})

def registro(request):
    return render(request, 'taller/Registro.html', {})

def base(request):
    return render(request, 'taller/Base.html', {})

def administrador(request):
    return render(request, 'taller/Administrador.html', {})
    
def mecanico(request):
    return render(request, 'taller/Mecanico.html', {})

def index2(request):
    return render(request, 'taller/Index2.html', {})

