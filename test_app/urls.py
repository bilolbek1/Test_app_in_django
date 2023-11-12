from django.urls import path
from .views import HomePageView, TestDetailView


urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("<int:id>", TestDetailView.as_view(), name='test_detail'),
]
