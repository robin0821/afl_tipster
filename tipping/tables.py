import django_tables2 as table
from django_tables2.utils import Accessor
from django_tables2.utils import A
from .models import tippings, tip_ladder
from django.utils.safestring import mark_safe

class TippingsTable(table.Table):


    class Meta:
        model = tip_ladder
        template_name = "django_tables2/bootstrap4-responsive.html"

        attrs = {'class': 'table'}
        fields = ('rank', 'full_name', 'total_tips', 'total_margin', 'avg_per_round')
