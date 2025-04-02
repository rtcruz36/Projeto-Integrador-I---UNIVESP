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
from django.contrib.auth.decorators import login_required

@login_required
def cadastrar_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MedicamentoForm()
    return render(request, 'cadastrar_medicamento.html', {'form': form})
@login_required
def editar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, pk=id)
    form = MedicamentoForm(request.POST or None, instance=medicamento)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'cadastrar_medicamento.html', {'form': form})


from django.contrib import messages
@login_required
def registrar_saida(request):
    if request.method == 'POST':
        id_medicamento = request.POST.get('medicamento_id')
        quantidade = int(request.POST.get('quantidade', 0))
        
        try:
            medicamento = Medicamento.objects.get(id=id_medicamento)
            if quantidade > 0 and quantidade <= medicamento.quantidade:
                medicamento.quantidade -= quantidade
                medicamento.save()
                messages.success(request, f'Saída de {quantidade} unidade(s) registrada para "{medicamento.nome}".')
            else:
                messages.error(request, 'Quantidade inválida ou superior ao estoque disponível.')
        except Medicamento.DoesNotExist:
            messages.error(request, 'Medicamento não encontrado.')

        return redirect('registrar_saida')

    medicamentos = Medicamento.objects.all()
    return render(request, 'registrar_saida.html', {'medicamentos': medicamentos})


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.is_active = False  # Será aprovado manualmente
            usuario.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})




