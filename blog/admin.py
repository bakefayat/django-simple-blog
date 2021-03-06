from django.contrib import admin
from .models import Blog, Category, Comment
from django.contrib import messages


@admin.action(description="انتشار مقالات انتخاب شده")
def make_published(modeladmin, request, queryset):
    queryset.update(status="p")
    modeladmin.message_user(request, "با موفقیت انتشار یافت", messages.SUCCESS)


@admin.action(description="پیش نویس مقالات انتخاب شده")
def make_draft(modeladmin, request, queryset):
    queryset.update(status="d")
    modeladmin.message_user(request, "با موفقیت پیش نویس شد", messages.SUCCESS)


@admin.action(description="ویژه سازی مقاله")
def make_special(modeladmin, request, queryset):
    queryset.update(is_special=True)
    modeladmin.message_user(request, "با موفقیت ویژه شد", messages.SUCCESS)


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "thumb",
        "author",
        "slug",
        "jpublished",
        "is_special",
        "status",
        "category_list",
    )
    # ordering = ['title', 'published']
    list_filter = ["category", "is_special"]
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_published, make_draft, make_special]
    readonly_fields = ("show_url",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "display", "parent")
    list_filter = ["display"]
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("body", "name", "email", "post", "display")
    list_filter = ["display"]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
