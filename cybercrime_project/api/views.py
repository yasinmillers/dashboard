from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import ComplaintForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def dashboard(request):
    complaints = Complaint.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"complaints": complaints})



@staff_member_required
def admin_dashboard(request):
    complaints = Complaint.objects.all()
    return render(request, "admin_dashboard.html", {"complaints": complaints})


from django.db.models import Count
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Complaint

@staff_member_required
def analytics(request):
    data = Complaint.objects.values('status').annotate(total=Count('id'))
    total_complaints = Complaint.objects.count()

    return render(request, "analytics.html", {
        "data": data,
        "total_complaints": total_complaints
    })