from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # Divide Post fields in sets
    fieldsets = [
        ('Post Details', {'fields': ['title', 'slug', 'author', 'body']}),
        ('Post Status', {'fields': ['publish', 'status',
                                    'created', 'updated']})
    ]

    # List of fields to be displyed in PostAdmin
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # Display title field as a link
    list_display_links = ('title',)
    # Adds List filter on the right site bar of the Post List page
    list_filter = ('status', 'created', 'publish', 'author')
    # Makes the status field editable on the Post List page
    list_editable = ('status',)
    # Sets the fields created and updated as readonly fields
    readonly_fields = ('created', 'updated',)
    # Adds a search list field on top of the Post List page
    search_fields = ('title', 'body')
    # Prepopulates slug field as you type the Post title
    prepopulated_fields = {'slug': ('title',)}
    # Makes the author field a searchable field in Post (replaces + add)
    raw_id_fields = ('author',)
    # Adds Bar to navigate quickly through a date hierarchy
    date_hierarchy = 'publish'
    # Adds list ordering by status and publish fields
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)
