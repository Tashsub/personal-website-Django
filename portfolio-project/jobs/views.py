from django.shortcuts import render

from .models import Job
# Create your views here.
def home(request): 

    #get all the job objects from the DB and use them as python code
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})