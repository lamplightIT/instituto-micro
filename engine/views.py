#coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from engine.forms import SubscriptionForm, ContactForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from courses.models import Course
from training_areas.models import TrainingArea
from news.models import Notice
from carousel_items.models import CarouselItem
from django.core.mail import send_mail

def home(request):
		c = Course.objects.all()
		ta = TrainingArea.objects.all()
		n = Notice.objects.all()
		ci = CarouselItem.objects.all()
		return render_to_response('index.html', RequestContext(request, {	'courses': c,
																																			'training_areas': ta,
																																			'news': n,
																																			'carousel_items': ci, }))

def sobre_o_instituto(request):
		return render_to_response('sobre_o_instituto.html', RequestContext(request))

@csrf_protect
def inscricoes(request):
		if request.method == 'POST':
				form = SubscriptionForm(request.POST)
				if form.is_valid():
						
						password = request.POST.get('password')
						email = request.POST.get('email')
						first_name = request.POST.get('first_name')
						last_name = request.POST.get('last_name')
						username = request.POST.get('username')
						
						user = User.objects.create_user(username, email, password)
						user.first_name = first_name
						user.last_name = last_name
						user.is_active = True

						user.save()
						body = 'Dados preenchidos pelo usuario: \n\n Nome: %s %s \n E-mail: %s \n Nome de Usuario: %s' % (user.first_name, user.last_name, user.email, user.username)
						body.encode('utf-8')
						send_mail(
										 'Instituto de Microscopia - Inscrição Online',
										 body,
										 'cursos@institutomicro.com.br',
										 ['cursos@institutomicro.com.br',])


						messages.success(request, 'Você foi cadastrado corretamente. Em breve entraremos em contato através do seu e-mail.')
						return redirect('/inscricoes/')
		else:
				form = SubscriptionForm()
		return render_to_response('inscricoes.html', RequestContext(request, {	'form': form,	}))

def servicos(request):
		return render_to_response('servicos.html', RequestContext(request))

@csrf_protect
def contato(request):
		if request.method == 'POST':
				form = ContactForm(request.POST)
				if form.is_valid():
						full_name = request.POST.get('full_name')
						email = request.POST.get('email')
						subject = request.POST.get('subject')
						msg = request.POST.get('msg')

						body = 'Dados preenchidos pelo usuario: \n\nNome: \n %s \n\nE-mail: \n %s \n\nMensagem: \n%s' % (full_name, email, msg)
						body.encode('utf-8')
						
						send_mail(
										 'Formulário de Contato Online - %s' % (subject),
										 body,
										 'cursos@institutomicro.com.br',
										 ['cursos@institutomicro.com.br',])

						messages.success(request, 'Sua mensagem foi enviada corretamente!')
						return redirect('/contato/')
		else:
				form = ContactForm()
		return render_to_response('contato.html', RequestContext(request, {	'form': form,	}))
		


