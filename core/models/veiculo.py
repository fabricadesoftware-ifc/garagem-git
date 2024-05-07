from django.db import models

class Veiculo(models.Model):
    descricao = models.CharField(max_length=100)
