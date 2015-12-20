from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import SignUpForm, ContactForm

# Create your views here.
def home(request):
	title = 'Hi Elisa'

	form = SignUpForm(request.POST or None)
	context = {
		'title' : title,
		'form' : form
	}


	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.full_name:
			instance.full_name = "Elisa"
		instance.save()
		context = {
			'title': "Thank You"
		}

	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	context = {
		'form' : form
	}

	if form.is_valid():
		email =  form.cleaned_data.get('email')
		full_name =  form.cleaned_data.get('full_name')
		message =  form.cleaned_data.get('message')
		subject = 'test 1'
		message = message + ' ' + email
		from_email = settings.EMAIL_HOST_USER
		to_email = [settings.EMAIL_HOST_USER]

		send_mail(subject, 
				  message, 
				  from_email, 
				  to_email,
				  fail_silently=False)

	return render(request, "forms.html", context)






