from apps.api.article.models import Article, Tag
from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ("author",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
