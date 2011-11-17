          # -*- coding: utf-8 -*-
import threading
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Pocket
from cabinet.models import Order
from forms import ClientForm, BaseClientFormset, OrderForm
from django.forms.models import inlineformset_factory
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
        ClientOrderFormset = inlineformset_factory(User, Order, exclude=('is_processed', 'pocket'), can_delete=False, formset=BaseClientFormset, extra=1)
        form = ClientForm()
        formset = ClientOrderFormset()
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
                formset = ClientOrderFormset(request.POST, instance = user)
                if formset.is_valid():
                    for f in formset.forms:
                        if f.is_valid():
                            obj = f.save()
                            obj.pocket = pocket
                            obj.save()
                    user = authenticate(username=user.email, password=password)
                    login(request, user)
                    t = threading.Thread(target= send_mail, args=[
                        u'Регистрация купиаудит ру', u'Логин:%s\nПароль:%s' % (user.username, password), 'info@my-spy.ru', [user.username], 'fail_silently=False'])
                    t.setDaemon(True)
                    t.start()
                    return HttpResponseRedirect("/cabinet")
                else:
                    user.delete()
    return render_to_response("main/pocket_page.html", locals(), context_instance=RequestContext(request))
