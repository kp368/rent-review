
from reviews import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
    url(r'^admin/$', views.index, name='index')
)
