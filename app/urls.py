from django.urls import path,include
from . import views

urlpatterns = [
   path("",views.InsertPage,name='insertpage'),
   path("insert/",views.Datainsertion,name='insert'),
   path("show/",views.Showpage,name='show'),
   #path("editpage/",views.update,name='editpage'),
   path("edit/<int:pk>",views.updatepage,name='edit'),
   path("sas/<int:pk>",views.update,name="sas"),
   path("delete/<int:pk>",views.Delete,name="delete")
]
