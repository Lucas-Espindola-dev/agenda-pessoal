from django.contrib import admin
from agenda.models import Compromissos


class CompromissoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'event_date',)
    search_fields = ('name', 'event_date',)


admin.site.register(Compromissos, CompromissoAdmin)

