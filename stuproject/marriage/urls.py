from django.urls import path,include
from marriage import views

urlpatterns = [
   path("",views.home,name="mary"),
   path("eli",views.eligibility,name="eli")
]