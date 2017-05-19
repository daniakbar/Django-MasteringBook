from django.contrib import admin
from .models import Publisher, Author, Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	search_fields = ('first_name', 'last_name')
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	list_filter =('publication_date',)
	date_hierarchy = ('publication_date')
	search_fields = ('title', 'publisher')
	fields = ('title', 'authors', 'publisher', 'publication_date') #mengganti list edit page
	filter_horizontal = ('authors',) #mengganti ke horisontal view hanya untuk database many to many
	raw_id_fields = ('publisher',) #jika publisher sudah banyak agar tidak lambat untuk menampilkan semua
class PublisherAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'city', 'website')
	search_fields = ('name',)


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
