from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class ProdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_show') # поля, которые мы хотим видеть
    list_display_links = ('id', 'title') # поля, на которые мы можем кликнуть и перейти по ним
    search_fields = ('title', 'content') # поля, по которым мы можем делать поиск
    fields = ('title','slug', 'price', 'about', 'photo','image_show', 'category') # поля, которые мы можем редактировать
    prepopulated_fields = {'slug':('title', )} # автоматическое формирование слага
    readonly_fields = ('image_show', )

    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src= '{}' width=60 />".format(obj.photo.url))
        return 'None'

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    fields = ('title','url_name', 'photo')

admin.site.register(Product, ProdAdmin)
admin.site.register(Menu, MenuAdmin)
