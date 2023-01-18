from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

from .models import Messages

class Index(TemplateView):
    template_name = "index.html"

class Contact(TemplateView):
    template_name = "contact.html"

    def post(self, request, *args, **kwargs):

        iName = request.POST['rName']
        iEmail = request.POST['rEmail']
        iPhone = request.POST['rPhone']
        iMessage = request.POST['rMessage']
 
        Messages.objects.create(CompanyName=iName, Email=iEmail, ContactPhone=iPhone, Message=iMessage)

        messages.success(request, '¡Mensaje Enviado!', extra_tags="contact_taital")
        messages.success(request, f'Responderemos a tu mensaje en las proximas 24 Horas', extra_tags="info-h6")
                  
        
        return redirect(reverse('Contact'))


