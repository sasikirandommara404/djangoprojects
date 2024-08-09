from django.urls import path,include
from scoreapp import views

urlpatterns = [
   path("",views.home,name="score"),
   path("score1",views.scorecal,name="score1")
]