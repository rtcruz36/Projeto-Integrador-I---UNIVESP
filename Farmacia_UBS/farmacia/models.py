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
    
# Create your models here.
