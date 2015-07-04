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
from .forms import SellerForm, PersonForm, BuyerMatchForm, BuyerCompletionForm

def index(request):
    ok = 'ezrego/index.html'
    return render(request, ok)

def loginv(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
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

@login_required(login_url='/govhack2015/loginv')
def buyavehicle(request):
    tmp = 'ezrego/buy.html'
    #uid = request.user.id
    #u = Person.objects.get(user_auth_id=uid)
    return render(request, tmp)

@login_required(login_url='/govhack2015/loginv')
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


def register(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            p1 = form.cleaned_data['personalorbusiness']
            p2 = form.cleaned_data['surname']
            p3 = form.cleaned_data['firstname']
            p4 = form.cleaned_data['companyname']
            p5 = form.cleaned_data['acn']
            p6 = form.cleaned_data['licencenumber']
            p7 = form.cleaned_data['dob']
            p8 = form.cleaned_data['homeaddress1']
            p9 = form.cleaned_data['homeaddress2']
            p10 = form.cleaned_data['homeaddresspostcode']
            p11 = form.cleaned_data['postaladdress1']
            p12 = form.cleaned_data['postaladdress2']
            p13 = form.cleaned_data['postaladdresspostcode']
            p14 = form.cleaned_data['phone']
            p15 = form.cleaned_data['email']
            p16 = form.cleaned_data['password']
            p = Person(
                personalorbusiness=p1,
                surname=p2,
                firstname=p3,
                companyname=p4,
                acn=p5,
                licencenumber=p6,
                dob=p7,
                homeaddress1=p8,
                homeaddress2=p9,
                homeaddresspostcode=p10,
                postaladdress1=p11,
                postaladdress2=p12,
                postaladdresspostcode=p13,
                phone=p14,
                email=p15,
            )
            AuthUser.objects.create_user(
                email=p15,
                password=p16,
            )
            ua = AuthUser.objects.get(email=p15)
            p.user_auth = ua
            p.save()
            return render(request, 'ezrego/register.html', {'thanks':1, 'email':p15})
        else:
            return render(request, 'ezrego/register.html', {'form':form})
    else:
        return render(request, 'ezrego/register.html', {'form':form})
