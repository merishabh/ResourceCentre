from django.conf.urls import url

from views import MemberView

urlpatterns = [
    url(r'^', MemberView.as_view()),
]