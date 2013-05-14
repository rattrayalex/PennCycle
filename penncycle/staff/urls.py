from django.conf.urls import patterns
from views import Dashboard

urlpatterns = patterns(
    '',
    (r'^/$', Dashboard.as_view()),
)
