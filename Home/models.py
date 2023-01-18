from django.db import models
from django.utils.translation import gettext_lazy as _

class Messages(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="ID")
    
    CompanyName = models.CharField(_("Usuario"),max_length=64)
    
    ContactPhone = models.CharField(_("Telefono"), max_length=64)
    Email = models.EmailField(_("E-mail"))
    
    Message = models.TextField(_("Mensaje"), max_length=512)
    
    Date = models.DateField(_("Fecha"), auto_now=False, auto_now_add=True)
    IsChecked = models.BooleanField(_("Estado"), default=False,
            help_text="Activar si el Mensaje se ha Verificado y Contestado")
    
    class Meta:
        verbose_name = _("Mensaje")
        verbose_name_plural = _("Mensajes")

    def __str__(self):
        return "Fecha Ingreso: %s" % self.Date