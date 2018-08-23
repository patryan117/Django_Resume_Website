from django.shortcuts import render
from resumeApp.models import *
from resumeApp.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages

def home(request):
	jobs = Job.objects.all().order_by('-start_date')
	executive_summary = GeneralInfo.objects.values('executive_summary').get()
	education_list = Education.objects.all().order_by('-year')
	skills = GeneralInfo.objects.values('skills').get()
	context = {
		'jobs': jobs,
		'executive_summary': executive_summary,
		'education_list': education_list,
		'skills': skills,
	}
	return render(request, 'index.html', context)

def contact(request):
	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get(
				'contact_name', '')
			contact_email = request.POST.get(
				'contact_email', '')
			form_content = request.POST.get('content', '')

			# Email the profile with the contact information
			template = get_template('contact_template.txt')
			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
			})
			content = template.render(context)

			email = EmailMessage(
				"New Form Submission",
				content,
				"peterdimaria.com" + '',
				['dimaria.p@gmail.com'],
				headers={'Reply-To': contact_email}
			)
			email.send()
			messages.success(request, 'Your message was sent to Peter.')
			return redirect('/contact/')

	return render(request, 'contact.html', {'form': form_class})

def about(request):
	about_copy = GeneralInfo.objects.values('about').get()
	context = {
		'about': about_copy
	}
	return render(request, 'about.html', context)

def privacy_policy(request):
	privacy_policy_copy = GeneralInfo.objects.values('privacy_policy').get()
	context = {
		'privacy_policy': privacy_policy_copy,
	}
	return render(request, 'privacy_policy.html', context)
