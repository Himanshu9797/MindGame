from django.conf.urls import url
from .views import signup, signup1

urlpatterns = [
    url(r'^signup$', signup.as_view())
]