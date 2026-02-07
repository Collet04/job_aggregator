# job_aggregator
A Django-based job aggregation platform that fetches and displays remote job listings with filtering, pagination, theming, and SEO-friendly job detail pages.

# Job Aggregator Platform

A production-ready Django web application that aggregates remote job listings and presents them in a clean, responsive, and user-friendly interface.

## Features

- Remote job aggregation and listing
- Multi-filtering (location, job type, tags)
- Pagination for large job datasets
- SEO-friendly job detail pages
- Light / Dark theme with persistence
- Responsive job cards layout
- User authentication with profile display
- Server-side caching for performance
- Production-ready deployment on Render

## Tech Stack

- **Backend:** Django
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (can be upgraded to PostgreSQL)
- **Deployment:** Render
- **Version Control:** Git & GitHub

## Installation (Local Setup)

```bash
git clone https://github.com/Collet04/job_aggregator.git
cd job_aggregator
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
