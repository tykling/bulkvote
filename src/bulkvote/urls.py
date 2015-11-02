from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bulkvote.views.frontpage', name='frontpage'),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name='contact'),
    url(r'^votes/(?P<uuid>[^/]+)/$', 'bulkvote.views.showvote', name='showvote'),
    url(r'^votes/(?P<uuid>[^/]+)/vote/$', 'bulkvote.views.vote', name='vote'),
    url(r'^votes/(?P<uuid>[^/]+)/results/$', 'bulkvote.views.vote_results', name='vote_results'),
]
