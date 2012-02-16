    # -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import Pocket

@login_required
def cabinet(request):
    user = User.objects.get(username=request.user.username)
    processed_orders = user.order_set.filter(is_processed=True)
    completed_orders = user.order_set.filter(is_processed=False)
    pockets = Pocket.objects.all()
    page_title = u"Личный кабинет - Купи-Аудит.ру"
    return render_to_response("cabinet/cabinet.html", locals(), context_instance=RequestContext(request))

def auth(request):
    page_title = u"Личный кабинет - Купи-Аудит.ру"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect("/cabinet")
        else:
            error = True
    return render_to_response("cabinet/login.html", locals(), context_instance=RequestContext(request))

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
