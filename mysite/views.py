from django.template.loader import get_template
from django.template import Template, Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from mysite.forms import ContactForm
from django.core.mail import send_mail
import datetime

def homepage(request):
	return HttpResponse("Dani Akbar")

def hello(request):
	return HttpResponse("Hello World")

# Menggunakan Templates Django di dalam View
# def timesnow(request):
# 	now = datetime.datetime.now()
# 	t = Template("<html><body>it is now {{ tanggal_sekarang }}</body></html>")
# 	html = t.render(Context({'tanggal_sekarang' : now}))
# 	return HttpResponse(html)

# Menggunakan Template Engine dari Luar/ Folder untuk lempar data datetime
def timesnow(request):
	now = datetime.datetime.now()
	return render(request, 'times-now1.html', {'tanggal_sekarang' : now}) #render page times-now1.html dan ambil data variabel now

# Menggunakan Templates dalam view
# def hours_ahead(request, nomerhalaman):
# 	try:
# 		nomerhalaman = int(nomerhalaman)
# 	except ValueError:
# 		raise Http404()
# 	dt = datetime.datetime.now() + datetime.timedelta(hours=nomerhalaman)
	
# 	html = "<html><body>in %s hour(s), it will be  %s. </body></html>" % (nomerhalaman, dt)
# 	return HttpResponse(html)

def hours_ahead(request, tambahanjam):
	try:
		tambahanjam = int(tambahanjam)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=tambahanjam)
	return render(request, 'hours-ahead.html', {'tambahanjam' : tambahanjam, 'next_time' : dt})

#From Contact bawaan Django

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get['email', 'noreply@example.com'],['siteowner@example.com'],
				)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
				initial={'subject': 'I Love Django!', 'message': 'Say Hello!'}
			)
	return render(request, 'contact-form.html', {'form': form})

