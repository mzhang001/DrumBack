import drumbackapp
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'dining_drum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('drumbackapp.urls'))
    # url(r'^polls/', include('polls.urls'))
]
