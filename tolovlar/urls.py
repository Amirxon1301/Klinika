from django.urls import path
from .views import *
urlpatterns = [
    path('hammasi/', TolovApiView.as_view()),
    path('admin_hammasi/', TolavAdminAPIView.as_view()),
]