from django.conf.urls import url

from views import ResoureBorrowView, ResoureReturnView

urlpatterns = [
	url(r'^borrow/', ResoureBorrowView.as_view()),
    url(r'^return/', ResoureReturnView.as_view()),
]