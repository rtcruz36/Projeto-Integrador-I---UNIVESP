from django.db import models
from django.utils import timezone

class Medicamento(models.Model):
    nome=models.CharField(max_length=100)
    lote=models.CharField(max_length=50)
    validade=models.DateField()
    quantidade=models.PositiveIntegerField()
    TIPO_CHOICES=[
        ('comum','Comum'),
        ('controlado','Controlado'),
        ('emergencia','Carrinho de Emergencia')
    ]
    tipo=models.CharField(max_length=20,choices=TIPO_CHOICES, default ='comum')

    def esta_vencido(self):
        return self.validade< timezone.now().date()

    def vencimento_proximo(self):
        dias_restantes=(self.validade-timezone.now().date).days
        return dias_restantes <= 30

    def __str__(self):
        return f"{self.quantidade} (Lote{self.lote})"


class SaidaMedicamento(models.Model):
    medicamento=models.ForeignKey(Medicamento,on_delete=models.CASCADE)
    quantidade=models.PositiveIntegerField()
    data_saida=models.DateTimeField(default=timezone.now)
    destino=models.CharField(max_length=100)
    foi_para_emergencia=models.BooleanField(default=False)

    def __str__(self):
        return f"saída de {self.quantidade}x {self.medicamento.nome} para {self.destino}"


    def save (self, *args, **kwargs):
        if self.medicamento.quantidade >= self.quantidade:
            self.medicamento.quantidade -= self.quantidade
            self.medicamento.save()
            super().save(*args, **kwargs)
        
        else:
            raise ValueError("Quantidade insuficiente em estoque para essa saída")
    
# Create your models here.

from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
        }
