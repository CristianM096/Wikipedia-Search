from django.urls import path
from .views import ReportListView
app_name="report"

urlpatterns=[
    path('reports/',ReportListView.as_view()),
]