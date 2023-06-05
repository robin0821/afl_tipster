import django_tables2 as table
from django_tables2.utils import Accessor
from django_tables2.utils import A
from .models import tippings

class TippingsTable(table.Table):

    class Meta:
        model = tippings
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id', 'email', 'picks', 'tips')