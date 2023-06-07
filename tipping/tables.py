import django_tables2 as table
from django_tables2.utils import Accessor
from django_tables2.utils import A
from .models import tippings
from django.utils.safestring import mark_safe

class TippingsTable(table.Table):


    class Meta:
        model = tippings
        template_name = "django_tables2/bootstrap4-responsive.html"

        attrs = {'class': 'table'}
        fields = ('first_name', 'last_name', 'picks', 'tips')