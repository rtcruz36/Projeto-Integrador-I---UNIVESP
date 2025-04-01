from django.shortcuts import render
from .models import Medicamento

def lista_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'farmacia/lista.html', {'medicamentos': medicamentos})

from django.http import HttpResponse

def home(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'home.html', {'medicamentos': medicamentos})


from django.shortcuts import render, redirect, get_object_or_404
from .forms import MedicamentoForm
from .models import Medicamento

def cadastrar_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MedicamentoForm()
    return render(request, 'cadastrar_medicamento.html', {'form': form})

def editar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, pk=id)
    form = MedicamentoForm(request.POST or None, instance=medicamento)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'cadastrar_medicamento.html', {'form': form})