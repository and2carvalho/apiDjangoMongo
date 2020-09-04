from django.db import models


class Autor(models.Model):

    nome = models.CharField('Nome', blank=False ,max_length=60)

    def __str__(self):
        return self.nome

class Noticia(models.Model):

    titulo = models.CharField('Título da Notícia', blank=False, max_length=120)
    texto = models.TextField('Texto da Notícia', blank=False)
    autor = models.ForeignKey(Autor, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
            return self.titulo