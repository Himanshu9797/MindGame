from django.conf.urls import url
from .views import signup, signup1, AppUserlogin

urlpatterns = [
    url(r'^signup$', signup.as_view()),
    url(r'^login$', AppUserlogin.as_view())
]