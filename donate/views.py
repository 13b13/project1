from django.shortcuts import render, redirect
from .models import Donate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    if request.method == 'GET':
        return render(request, 'donate/donate.html')
    else:
        name = request.POST.get('name')
        kind = request.POST.get('kind')
        condition = request.POST.get('condition')
        upgrade = request.POST.get('upgradee')
        last_update = request.POST.get('last_update')
        Donate.objects.create(
            name=name,
            kind=kind,
            condition=condition,
            upgrade=upgrade,
            last_update=last_update
        )
        return redirect('/')


def education(request):
    return render(request, 'frontend/html/information-sharing.html')

# def mydevice(request):
#     donate = Donate.objects
#     return render(request, 'html/my_device.html', {'donate' : donate})