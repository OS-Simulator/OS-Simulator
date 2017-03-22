from django.contrib import admin

# Register your models here.
from .models import ProcessSchedAlg, Adv

class AdvInline(admin.TabularInline):
    model = Adv
    extra = 3

class ProcessSchedAlgAdmin(admin.ModelAdmin):

    inlines = [AdvInline]

admin.site.register(ProcessSchedAlg, ProcessSchedAlgAdmin)
