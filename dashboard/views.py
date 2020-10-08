from django.shortcuts import render
from django.http import JsonResponse
from .services import my_data
from django.core import serializers
from dashboard.models import Order


# getting my_data() from the service.py
def dashboard_with_pivot(request):
    return render(request, 'dashboard.html', {'datas': my_data()})


# just to show the data in json format
def pivot_data(request):
    return JsonResponse(my_data(), safe=False)

# def pivot_data(request):
#     dataset = Order.objects.all()
#     data = serializers.serialize('json', dataset)
#     return JsonResponse(data, safe=False)
