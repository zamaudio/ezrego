from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.forms import AuthenticationForm

from .models import Vehicle, Person, VehicleTransfer
from .forms import SellerForm, BuyerForm

def index(request):
    ok = 'ezrego/index.html'
    return render(request, ok)

def loginv(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=emailorname, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'registration/login.html', {'badlogin':1, 'form':form})
    else:
        return render(request, 'registration/login.html', {'form':form})

def logoutv(request):
    if request.user.is_authenticated():
        logout(request)
    return HttpResponseRedirect('/')

def buyavehicle(request):
    tmp = 'ezrego/buy.html'
    #uid = request.user.id
    #u = Person.objects.get(user_auth_id=uid)
    return render(request, tmp)

#@login_required(login_url='/loginv')
def sellerintent(request):
    if request.method == 'POST':
        uid = request.user.id
        u = Person.objects.get(user_auth_id=uid)
        form = SellerForm(request.POST)
        if form.is_valid():
            person = Person(
                personalorbusiness=form.cleaned_data['personalorbusiness']
                )
            person.save()
            return HttpResponseRedirect('sellerthankyou')
    else:
        form = SellerForm()

    return render(request, 'ezrego/sell.html', {'form': form})
