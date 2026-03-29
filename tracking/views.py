from django.shortcuts import render
from reports.models import Issue

def view_reports(request):
    issues = Issue.objects.all().order_by('-created_at')  
    return render(request, 'view_reports.html', {'issues': issues})
