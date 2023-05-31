from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return self.nome_funcionario

class Dvd(models.Model):
    titulo = models.CharField(max_length=250)
    texto = models.TextField()
    valor = models.FloatField()

    def __str__(self):
        return self.titulo

class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_cidade

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_cliente

class Reserva(models.Model):
    data_reserva = models.DateField()
    data_entrega = models.DateTimeField()
    valor = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    dvd = models.ManyToManyField(Dvd)
