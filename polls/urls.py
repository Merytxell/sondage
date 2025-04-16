from django.urls import path
from . import views

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('all/', views.AllView.as_view(), name='all'),
    path('<int:question_id>/frequency/',views.frequency, name='frequency'),
    path('statistics/', views.statistics, name='statistics'),

]
