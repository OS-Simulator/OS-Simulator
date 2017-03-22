from django.contrib import admin

# Register your models here.
from .models import SynchroAlg, Adv

class AdvInline(admin.TabularInline):
    model = Adv
    extra = 3

class SynchroAlgAdmin(admin.ModelAdmin):

    inlines = [AdvInline]

admin.site.register(SynchroAlg, SynchroAlgAdmin)
