from django.contrib import admin
from detail.models import Detail

class DetailAdmin(admin.ModelAdmin):
    list_display=('name','number','city','standard','goal')
admin.site.register(Detail,DetailAdmin)
# Register your models here.
