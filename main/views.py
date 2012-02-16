          # -*- coding: utf-8 -*-
import threading
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Pocket
from cabinet.models import Order
from forms import ClientForm, OrderForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail

def index(request):
    pockets = Pocket.objects.all()
    return render_to_response("main/index.html", locals(), context_instance=RequestContext(request))

def time(request):
    return render_to_response("main/time.html", locals(), context_instance=RequestContext(request))

def money(request):
    return render_to_response("main/money.html", locals(), context_instance=RequestContext(request))

def faq(request):
    return render_to_response("main/faq.html", locals(), context_instance=RequestContext(request))

def about(request):
    return render_to_response("main/about.html", locals(), context_instance=RequestContext(request))

def pocket(request, pocket_slug):
    pocket = Pocket.objects.get(slug=pocket_slug)
    if request.user.is_authenticated():
        form = OrderForm()
    else:
        form = ClientForm()
    if request.method == 'POST':
        if request.user.is_authenticated():
            form = OrderForm(request.POST)
            if form.is_valid():
                newform = form.save(commit=False)
                newform.client = request.user
                newform.pocket = pocket
                newform.save()
                return HttpResponseRedirect("/cabinet")
        else:
            form = ClientForm(request.POST)
            if form.is_valid():
                password = User.objects.make_random_password()
                user = User.objects.create_user(username=form.cleaned_data['email'], email=form.cleaned_data['email'], password=password)
                user.groups.add(1)
                user.first_name = form.cleaned_data['name']
                user.save()
                order = Order()
                order.domen = form.cleaned_data['domen']
                order.contacts = form.cleaned_data['contacts']
                order.keywords = form.cleaned_data['keywords']
                order.reason = form.cleaned_data['reason']
                order.comment = form.cleaned_data['comment']
                order.client = user
                order.is_processed = True
                order.pocket = pocket
                order.save()
                user = authenticate(username=user.email, password=password)
                login(request, user)
                t = threading.Thread(target= send_mail, args=[
                    u'Доступ в личный кабинет Купи-Аудит.ру', u'Здравствуйте. Спасибо за заказ аудита в сервисе Купи-Аудит.ru\n\n\
                    Ваши данные для входа в личный кабинет:\nлогин:%s\nпароль:%s' % (user.username, password), 'info@kupiauditru', [user.username], 'fail_silently=false'])
                t.setDaemon(True)
                t.start()
                return HttpResponseRedirect("/cabinet")
    return render_to_response("main/pocket_page.html", locals(), context_instance=RequestContext(request))

