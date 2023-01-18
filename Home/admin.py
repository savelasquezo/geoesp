from django.contrib import admin

from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .models import Messages

admin.site.unregister(Group)

class GEAdminSite(admin.AdminSite):
    index_title = 'Panel Administrativo'
    verbose_name = "GEOESP"

admin_site = GEAdminSite()
admin.site = admin_site

admin_site.site_header = "GEOESP"


class MessagesAdmin(admin.ModelAdmin):
    
    #def display_object(self, obj):
    #    return "Mensaje: %s" % obj.nombre
    
    list_display = (
        "id",
        "CompanyName",
        "ContactPhone",
        "Email",
        "Date",
        "IsChecked"
        )

    dInformation = {"fields": (
            ("CompanyName","IsChecked"),
            ("Email","ContactPhone"),
            "Message"
        )}

    fieldsets = (
        ("Informacion", dInformation),)

    list_filter = ["CompanyName","Date","IsChecked"]
    search_fields = ['CompanyName']
    
    def has_add_permission(self, request, obj=None):
            return False

admin.site.register(Messages, MessagesAdmin)