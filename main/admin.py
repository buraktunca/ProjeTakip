from django.contrib import admin
from main.models import Project,Person,autority,indic
# Register your models here.
class projectadmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("project_name",)}
    list_display = (
    'pk',
    'project_name',
    'project_start',
    'project_finish',
    'project_budget',

    )
    list_filter = ('project_name',)
    list_editable = ('project_name','project_start','project_finish','project_budget')

class personadmin(admin.ModelAdmin):

    list_display = (
    'pk',
    'name',
    'surname',
    'email',

    )

    list_editable = ('name','surname','email',)

class autorityadmin(admin.ModelAdmin):

    list_display = (
    'pk',
    'proje',
    'person',
    'role',
    'tm'

    )

    list_editable = ('proje','person','role','tm',)

class indicatoradmin(admin.ModelAdmin):

    list_display = (
    'pk',
    'proje',
    'indikator_name'

    )



admin.site.register(Project,projectadmin)
admin.site.register(Person,personadmin)
admin.site.register(autority,autorityadmin)
admin.site.register(indic,indicatoradmin)
