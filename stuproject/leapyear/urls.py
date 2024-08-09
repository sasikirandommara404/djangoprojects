from django.urls import path,include
from leapyear import views

urlpatterns = [
   path("",views.home,name="leap"),
   path("che",views.leapchecking,name="che")
]