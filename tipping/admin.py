from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import AFLTeams, tippings, AFLFixture
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportMixin, ExportMixin
admin.site.site_header = 'intelia AFL Tipster'

# Register your models here.
class AFLTeamsResources(resources.ModelResource):

    class Meta:
        model = AFLTeams

class tippingsResources(resources.ModelResource):

    class Meta:
        model = tippings

class FixtureResource(resources.ModelResource):
    
    class Meta:
        model = AFLFixture

class AFLTeamsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'logo')
    readonly_fields = ('id', 'name', 'logo')
    resource_class = AFLTeamsResources

class tippingsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'hteam', 'ateam', 'winner', 'localtime')
    readonly_fields = ('id', 'hteam', 'ateam', 'winner', 'localtime')
    resource_class = tippingsResources

class FixtureAdmin(ImportExportModelAdmin):
    list_display = ('id', 'hteam', 'ateam', 'winner', 'localtime', 'complete', 'updated', 'hgoals', 'agoals', 'date', 'venue')
    readonly_fields = ('id', 'hteam', 'ateam', 'winner', 'localtime', 'date')
    list_filter = ('roundname', 'hteamid', 'date')
    resource_class = FixtureResource

admin.site.register(AFLTeams, AFLTeamsAdmin)
admin.site.register(AFLFixture, FixtureAdmin)
admin.site.register(tippings)