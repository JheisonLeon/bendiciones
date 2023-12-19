from django.db import models
from urllib.parse import urlparse, parse_qs
from enum import Enum

class TipoSalud(Enum):
    EJERCICIO = 'EJERCICIO'
    NUTRICION = 'NUTRICION'

class Salud(models.Model):
    id= models.AutoField(primary_key=True)
    title=models.CharField(verbose_name='Titulo', max_length=100)
    description=models.CharField(verbose_name='Descripcion', max_length=1000, null=True)
    url=models.CharField(verbose_name='Link del video', max_length=1000)
    date = models.DateTimeField(verbose_name='Fecha', auto_now_add=True)
    video_code = models.CharField(verbose_name='Código del video', max_length=50, blank=True, null=True)
    tipo = models.CharField(verbose_name='Tipo de Salud', max_length=10, choices=[(tag.name, tag.value) for tag in TipoSalud], default=TipoSalud.EJERCICIO.value)

    def save(self, *args, **kwargs):
        # Extraer el código del video de la URL
        video_url = self.url
        parsed_url = urlparse(video_url)

        if 'youtube.com' in parsed_url.netloc:
            video_code = parse_qs(parsed_url.query).get('v', [None])[0]
        elif 'tiktok.com' in parsed_url.netloc:
            path_segments = parsed_url.path.strip('/').split('/')
            video_code = path_segments[-1] if path_segments else None
        else:
            video_code = None

        self.video_code = video_code
        super().save(*args, **kwargs)

    def __str__(self):
        res = self.title
        video_url = self.url
        parsed_url = urlparse(video_url)

        if 'youtube.com' in parsed_url.netloc:
            res = 'Youtube - ' + self.title
        elif 'tiktok.com' in parsed_url.netloc:
            res = 'Tiktok - ' + self.title
        else:
            res = self.title
         
        return res