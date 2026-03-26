
from django.shortcuts import render

def report_issue(request):
    return render(request, 'report_issue.html')