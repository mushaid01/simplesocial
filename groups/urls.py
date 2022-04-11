from django.urls import path

from . import views

app_name = 'groups'

urlpatterns = [
    path(r"^$", views.ListGroups.as_view(), name="all"),
    path(r"^new/$", views.CreateGroup.as_view(), name="create"),
    path(r"^posts/in/(?P<slug>[-\w]+)/$",views.SingleGroup.as_view(),name="single"),
    path(r"join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    path(r"leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),
]
