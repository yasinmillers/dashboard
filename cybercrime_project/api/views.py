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