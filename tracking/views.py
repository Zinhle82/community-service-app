from django.shortcuts import render

def view_reports(request):
    return render(request, 'view_reports.html')
