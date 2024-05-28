from django.contrib import admin
from .models import Results


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(result=0)

class CoinAdmin(admin.ModelAdmin):
    list_display = ('result',)

# Register your models here.
admin.site.register(Results, CoinAdmin)
