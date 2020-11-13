from django.contrib import admin
from practice_app.models import Entry,Author,Blog

class EntryAdmin(admin.ModelAdmin):
    list_display = ['blog', 'headline','authors']
    ordering = ['pub_date']

    # def get_authors_name(self, obj):
    #     return "\n".join([p.name for p in obj.Author.all()])

admin.site.register(Entry)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','email')

admin.site.register(Author, AuthorAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name','tagline')

admin.site.register(Blog, BlogAdmin)


