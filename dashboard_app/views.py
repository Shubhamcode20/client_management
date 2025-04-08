from datetime import timedelta

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now
from .models import ClientProfile, Appointment
from .forms import ClientForm


def dashboard(request):
    two_months_ago = now() - timedelta(days=60)
    new_clients_count = ClientProfile.objects.filter(created_at__gte=two_months_ago).count()
    new_appointments_count = Appointment.objects.filter(appointment_datetime__gte=two_months_ago).count()
    context = {
        'new_clients_count': new_clients_count,
        'new_appointments_count': new_appointments_count,
    }
    return render(request, 'dashboard_app/dashboard.html', context)

def api_clients(request):
    two_months_ago = now() - timedelta(days=60)
    clients = ClientProfile.objects.filter(created_at__gte=two_months_ago)
    data = list(clients.values('id', 'name', 'primary_number', 'country_code', 'created_at'))
    return JsonResponse(data, safe=False)

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
