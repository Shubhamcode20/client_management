from datetime import timedelta

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.timezone import now
from .models import ClientProfile, Appointment
from .forms import ClientForm
from django.core.paginator import Paginator

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
    search = request.GET.get('search', '')
    offset = int(request.GET.get('offset', 0))
    limit = int(request.GET.get('limit', 10))

    clients = ClientProfile.objects.filter(name__icontains=search).order_by('-created_at')
    paginator = Paginator(clients, limit)
    page_number = (offset // limit) + 1
    page = paginator.get_page(page_number)

    rows = [
        {
            "id": client.id,
            "name": client.name,
            "primary_number": client.primary_number,
            "country_code": client.country_code,
            "created_at": client.created_at.strftime('%d-%m-%Y %H:%M:%S'),
        }
        for client in page.object_list
    ]

    return JsonResponse({
        'total': paginator.count,
        'rows': rows,
    })

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
