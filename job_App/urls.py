from django.urls import path
from .views import job_list_view, job_detail_view

urlpatterns = [
    path("", job_list_view, name="job_list"),
    path("job/<int:job_id>/", job_detail_view, name="job_detail"),
]
