from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import AFLTeams, tippings, AFLFixture, AFLLadder, tip_ladder
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

class AFLLadderResource(resources.ModelResource):

    class Meta:
        model = AFLLadder

class tippingLadderResource(resources.ModelResource):

    class Meta:
        model = tip_ladder

class AFLTeamsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'logo')
    readonly_fields = ('id', 'name', 'logo')
    resource_class = AFLTeamsResources

class tippingsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'round', 'first_name', 'last_name', 'email', 'hteam', 'ateam', 'winner', 'date', 'picks', 'fixture_id', 'status', 'tips', 'margin_diff', 'margin', 'has_margin')
    readonly_fields = ('id', 'round', 'first_name', 'last_name', 'email', 'hteam', 'ateam', 'winner', 'date', 'picks', 'fixture_id', 'status', 'tips', 'margin_diff', 'margin', 'has_margin')
    resource_class = tippingsResources

class FixtureAdmin(ImportExportModelAdmin):
    list_display = ('id', 'hteam', 'ateam', 'winner', 'localtime', 'complete', 'updated', 'hgoals', 'agoals', 'hscore', 'ascore', 'date', 'venue')
    readonly_fields = ('id', 'hteam', 'ateam', 'winner', 'localtime', 'date')
    list_filter = ('roundname', 'hteamid', 'date')
    resource_class = FixtureResource

class AFLLadderAdmin(ImportExportModelAdmin):
    list_display = ('pos', 'club',  'played', 'wins', 'losses', 'draws', 'pts', 'logo')
    readonly_fields = ('pos', 'club', 'played', 'wins', 'losses', 'draws', 'pts', 'logo')
    resource_class = AFLLadderResource

class tippingLadderAdmin(ImportExportModelAdmin):
    list_display = ('rank', 'email', 'full_name', 'total_tips', 'total_margin', 'avg_per_round', 'last_round_tips',
                    'last_round_margin')
    readonly_fields = ('rank', 'email', 'full_name', 'total_tips', 'total_margin', 'avg_per_round', 'last_round_tips',
                    'last_round_margin')
    list_filter = ('email', 'rank')
    resource_class = tippingLadderResource

admin.site.register(AFLTeams, AFLTeamsAdmin)
admin.site.register(AFLFixture, FixtureAdmin)
admin.site.register(tippings, tippingsAdmin)
admin.site.register(AFLLadder, AFLLadderAdmin)
admin.site.register(tip_ladder, tippingLadderAdmin)