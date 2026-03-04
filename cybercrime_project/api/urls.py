from django.urls import path
from .views import RegisterView, LoginView, ComplaintCreateView, ComplaintListView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("complaint/", ComplaintCreateView.as_view(), name="complaint"),
    path("dashboard/", ComplaintListView.as_view(), name="dashboard"),
]