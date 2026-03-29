from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Issue

def report_issue(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')

        Issue.objects.create(
            title=title,
            description=description,
            location=location
        )

        messages.success(request, "Issue reported successfully!")
        return redirect('/reports/')   

    return render(request, 'report_issue.html')
