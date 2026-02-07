from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page

@login_required
@cache_page(60 * 10)  # cache for 10 minutes
def job_list_view(request):
    user = request.user

    # Ensure the user has a profile
    if not hasattr(user, "profile"):
        from accounts.models import Profile
        Profile.objects.create(user=user)

    profile = user.profile

    # Force profile completion
    if not user.first_name or not user.last_name or not profile.profile_image:
        return redirect("profile")
    
#------------------Job_Section-------------------------#
    url = "https://remotive.com/api/remote-jobs"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        jobs = data.get("jobs", [])

        location = request.GET.get("location")
        job_type = request.GET.get("job_type")
        tag = request.GET.get("tag")
        search = request.GET.get("search")

        filtered_jobs = jobs

        if location:
            filtered_jobs = [
                job for job in filtered_jobs
                if location.lower() in job["candidate_required_location"].lower()
            ]

        if job_type:
            filtered_jobs = [
                job for job in filtered_jobs
                if job_type.lower() in job["job_type"].lower()
            ]

        if tag:
            filtered_jobs = [
                job for job in filtered_jobs
                if tag.lower() in [t.lower() for t in job["tags"]]
            ]

        if search:
            filtered_jobs = [
                job for job in filtered_jobs
                if search.lower() in job["title"].lower()
                or search.lower() in job["company_name"].lower()
            ]

        paginator = Paginator(filtered_jobs, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "jobs/job_list.html",
            {"page_obj": page_obj}
        )

    except requests.exceptions.RequestException:
        return render(
            request,
            "jobs/job_list.html",
            {"error": "Jobs are temporarily unavailable."}
        )

def job_detail_view(request, job_id):
    url = "https://remotive.com/api/remote-jobs"
    response = requests.get(url)
    data = response.json()
    jobs = data.get("jobs", [])

    job = next((j for j in jobs if j["id"] == job_id), None)

    if not job:
        return render(request, "jobs/404.html", status=404)

    return render(request, "jobs/job_detail.html", {"job": job})

def custom_404_view(request, exception):
    return render(request, "Error_Page/404.html", status=404)