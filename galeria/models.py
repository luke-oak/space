from django.db import models

#Classes que serão convertidas nas tabelas do banco

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)


#retorna o nome do objeto
    def __str__(self):
        return f"Fotografia [nome={self.nome}"