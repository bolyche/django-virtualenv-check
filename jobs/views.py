from django.shortcuts import render

from .models import Job

def home(request):
    jobs = Job.objects
    worddictionary = {'why','is','this','erroring'}
    print(worddictionary)
    for item in Job.objects.all():
        print(item.summary)
    return render(request, 'jobs/home.html', {'jobs':jobs})
