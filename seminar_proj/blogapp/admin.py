from django.contrib import admin
from .models import Author
@admin.action(description='Тестовый action')
def admintest(modeladmin, request, queryset):
    queryset.update(first_name='test_name')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name',)
    list_filter = ('last_name',)
    search_fields = ('first_name','last_name',)

    readonly_fields = ['biography', 'birthday']
    actions = [admintest,]

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['first_name', 'last_name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Об авторе',
                'fields': ['biography', 'birthday'],
            },
        ),
    ]

admin.site.register(Author,AuthorAdmin)
