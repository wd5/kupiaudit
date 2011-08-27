from django.conf.urls.defaults import *

urlpatterns = patterns('',
                      url(r'^$', 'cabinet.views.cabinet', name="cabinet-page"),
                      url(r'/login$', 'cabinet.views.auth', name="login-page"),
                      url(r'/logout$', 'cabinet.views.logout_view', name="logout-page"),
)