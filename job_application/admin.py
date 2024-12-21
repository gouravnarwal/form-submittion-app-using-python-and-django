from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email")
    search_fields = ("first_name","last_name","email")
    list_filter = ("date","occupation")
    ordering = ("first_name",)
    readonly_fields = ("first_name","last_name","email","occupation","date")

admin.site.register(Form,FormAdmin)  #This tells Django to use the configurations defined in FormAdmin when displaying and managing the Form model in the admin interface.
