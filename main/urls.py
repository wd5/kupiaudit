from django.conf.urls.defaults import *

urlpatterns = patterns('',
                      url(r'^$', 'main.views.index', name="main-page"),
                      url(r'^time$', 'main.views.menu', name="menu-page"),
                      url(r'^money$', 'main.views.menu', name="menu-page"),
                      url(r'^faq$', 'main.views.menu', name="menu-page"),
                      url(r'^about$', 'main.views.menu', name="menu-page"),
                      url(r'^(?P<pocket_slug>[-\w]+)$', 'main.views.pocket', name="pocket-page"),
)
