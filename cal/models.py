from django.db import models
from django.urls import reverse

PROF=(
        ('SDL | Mme. Azam', 'Mme. Azam'),
        ('SD8 | Mme. Lannes', 'Mme. Lannes'),
        ('SD9 | Mme. Kelly', 'Mme. Kelly'),
        ('SD7 | M. El Hammouchi', 'M. El Hammouchi')
    )
class Event(models.Model):
    prof = models.CharField(max_length=200, choices=PROF, default='Non défini')
    du = models.DateTimeField()
    au = models.DateTimeField()
    contenu = models.CharField(max_length=200, default='Non défini')
    inscrits = models.TextField(default='Indiquez les informations suivantes :\nNOM Prénom Classe Groupe')
 
    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.prof} </a>'
