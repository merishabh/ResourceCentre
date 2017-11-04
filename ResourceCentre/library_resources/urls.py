from django.conf.urls import url

from views import BookView

urlpatterns = [
    url(r'^', BookView.as_view()),
]