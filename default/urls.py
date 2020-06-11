from django.urls import path
from . import views

urlpatterns = [
   # path('poll/', views.poll_list),
    path('poll/', views.PollList.as_view()),
    path('poll/<int:pk>/',views.PollView.as_view()),
    path('option/<int:oid>/',views.PollVote.as_view()),
    path('poll/create/', views.Pollcreate.as_view()),
    path('poll/<int:pk>/edit/' , views.PollEdit.as_view()),
    path("poll/<int:pid>/delete/", views.OptionDelete.as_view()),
    path("option/<int:pk>/delete/",views.OptionDelete.as_view()),
    path('poll/<int:pk>/add',views.Optioncreate.as_view()),
    path('option/<int:pk>/edit/',views.OptionEdit.as_view()),
]
