from django.conf.urls import url
from django.views.generic import TemplateView

app_name = "drumbackapp"

urlpatterns = [
    url(r'^start$', TemplateView.as_view(template_name='start.html'), name='start'),
    url(r'^drum', TemplateView.as_view(template_name='drum.html'), name='drum'),
    url(r'^index', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^thanks', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
    url(r'^challengemode', TemplateView.as_view(template_name='challengemode.html'), name='challengemode')
]