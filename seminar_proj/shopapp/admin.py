from django.contrib import admin
from .models import Image, Customer, Product, Order


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number',)
    list_filter = ('name',)
    search_fields = ('name',)

    readonly_fields = ['address', 'registration_date']


    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', ],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'О клиенте',
                'fields': ['registration_date','phone_number', 'address'],
            },
        ),
    ]



@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'description', 'quantity']
    ordering = ['added_date', '-quantity']
    list_filter = ['added_date', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    """Отдельный продукт."""
    # fields = ['name', 'description', 'date_added','rating']
    readonly_fields = ['name', ]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields':['description'],
        },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],

            }
        ),

    ]


admin.site.register(Image)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)