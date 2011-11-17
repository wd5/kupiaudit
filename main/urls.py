from django.conf.urls.defaults import *

urlpatterns = patterns('',
                      url(r'^$', 'main.views.index', name="main-page"),
                      url(r'^time$', 'main.views.time', name="time-page"),
                      url(r'^money$', 'main.views.money', name="money-page"),
                      url(r'^faq$', 'main.views.faq', name="faq-page"),
                      url(r'^about$', 'main.views.about', name="about-page"),
                      url(r'^(?P<pocket_slug>[-\w]+)$', 'main.views.pocket', name="pocket-page"),
)
