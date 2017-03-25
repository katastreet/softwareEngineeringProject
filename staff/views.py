from django.shortcuts import render
from django.http import JsonResponse
from public.models import OfficeData
from django.utils import timezone

# Create your views here.


def analysis(request):
    return render(request, 'staff/analyse.html', {})


def getdataforchart(request):
    year = timezone.now().year
    labels = []
    sales = []
    for i in range(year-10, year+1):
        labels += [i]
        valid = OfficeData.objects.filter(boughtdate__year=i)
        default = sum([d.boughtprice*d.quantity for d in valid])
        sales += [default]

    data = {
            "labels": labels,
            "defaultData": sales,
    }
    return JsonResponse(data)
