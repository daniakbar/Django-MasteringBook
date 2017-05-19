from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from books.models import Book
# Create your views here.

def search_form(request):
	return render(request, 'search-form.html')

# def search(request):
# 	if 'q' in request.GET:
# 		message = 'Yous Search for %r' % request.GET['q']
# 	else:
# 		message = 'Your search is an empty form.'
# 	return HttpResponse(message)

# Cara Menerima Data dengan Get, dan melempar data ke halaman search-form.html dengan cek pakai if
def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Masukkan Kata yg inggin di Cari terlebih dahulu')
		elif len(q) > 50:
			errors.append('Judul Buku cuma 50 Karakter ya gan :v')
		else:
			books = Book.objects.filter(title__icontains =q)
			return render(request, 'search-result.html', {'books': books, 'query': q})
	return render(request, 'search-form.html', {'errors' : errors})