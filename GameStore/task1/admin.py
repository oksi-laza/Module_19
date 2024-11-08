from django.contrib import admin
from .models import Category, News

# Админка для модели Category
@admin.register(Category)    # в декораторе указываем нашу модель
class CategoryAdmin(admin.ModelAdmin):    # назовем класс с названием, отражающем нашу модель Category. 'list_display' - обязательное поле
    list_display = ('name',)    # Поля для отображения в списке (в виде кортежа), можно указывать из модели не все поля, можно все или часть
    search_fields = ('name',)    # Поля для поиска (в виде кортежа)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_published')
    list_filter = ('category', 'is_published')    # Фильтрация по категории и статусу публикации
    search_fields = ('title', 'content')    # Поля для поиска
    list_per_page = 10    # Количество новостей на странице

    # Разделение полей на секции. None - это поля, которые не нужно разбивать на секции
    fieldsets = (
        ('НОВОСТИ', {
            'fields': ('title', 'content', 'category')
        }),
        ('Дополнительные настройки', {
            'classes': ('collapse',),
            'fields': ('is_published', 'created_at', 'updated_at')
        }),
    )

    # Поля только для чтения, без редактирования
    readonly_fields = ('created_at', 'updated_at')
