from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.forms import AuthenticationForm
import hashlib

from .models import Vehicle, Person, VehicleTransfer
from .forms import SellerForm, PersonForm, BuyerMatchForm, BuyerCompletionForm

def index(request):
    ok = 'ezrego/index.html'
    if request.user:
        return render(request, ok, {'userloggedin':request.user})
    else:
        return render(request, ok)

def loginv(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/govhack2015')
        else:
            return render(request, 'registration/login.html', {'badlogin':1, 'form':form})
    else:
        return render(request, 'registration/login.html', {'form':form})

def logoutv(request):
    if request.user.is_authenticated():
        logout(request)
    return HttpResponseRedirect('/govhack2015')

@login_required(login_url='/govhack2015/loginv')
def buyavehicle(request):
    tmp = 'ezrego/buy.html'
    #uid = request.user.id
    #u = Person.objects.get(user_auth_id=uid)
    return render(request, tmp)

@login_required(login_url='/govhack2015/loginv')
def sellerthankyou(request):
    tmp = 'ezrego/sellerthankyou.html'
    uid = request.user.id
    u = Person.objects.get(user_auth_id=uid)
    return render(request, tmp, {'seller':u})

@login_required(login_url='/govhack2015/loginv')
def sellerintent(request):
    if request.method == 'POST':
        uid = request.user.id
        u = Person.objects.get(user_auth_id=uid)
        form = SellerForm(request.POST)
        if form.is_valid():
            v = Vehicle(
                current_rego=form.cleaned_data['current_rego'],
                rego_expiry=form.cleaned_data['rego_expiry'],
                vehicle_year=form.cleaned_data['vehicle_year'],
                vehicle_model=form.cleaned_data['vehicle_model'],
                vehicle_bodytype=form.cleaned_data['vehicle_bodytype'],
                vehicle_vin=form.cleaned_data['vehicle_vin'],
                is_pre1989=form.cleaned_data['is_pre1989'],
                is_written_off=form.cleaned_data['is_written_off'],
                is_rwc_attached=form.cleaned_data['is_rwc_attached'],
                rwc_serialnumber=form.cleaned_data['rwc_serialnumber'],
                rwc_issuedate=form.cleaned_data['rwc_issuedate'],
                rwc_testerlicence=form.cleaned_data['rwc_testerlicence']
            )
            v.save()

            tcode=hashlib.md5("".join([str(v.vehicle_vin), str(u.email)])).hexdigest()
            tcode=tcode[1:9]

            t = VehicleTransfer(
                seller=u,
                vehicle=v,
                market_value=form.cleaned_data['market_value'],
                date_of_sale=form.cleaned_data['date_of_sale'],
                transfer_fee=form.cleaned_data['transfer_fee'],
                duty_fee=form.cleaned_data['duty_fee'],
                transfer_code=tcode
            )
            t.save()
            return render(request, 'ezrego/sellerthankyou.html', {'tcode':t.transfer_code})
    else:
        form = SellerForm()

    return render(request, 'ezrego/sell.html', {'form': form})

@login_required(login_url='/govhack2015/loginv')
def buyavehicle(request):
    if request.method == 'POST':
        if request.POST.has_key('state'):
            if request.POST['state'] == '0':
                form = BuyerMatchForm(request.POST)
                if form.is_valid():
                    try:
                        t = VehicleTransfer.objects.get(transfer_code=form.cleaned_data['transfer_code'])
                        return render(request, 'ezrego/buyavehicle.html', {'state1':1, 'tcode':t.transfer_code})
                    except:
                        t = {}
                        return render(request, 'ezrego/buyavehicle.html', {'state0':1, 'form':form, 'failed':1})

                else:
                    form = BuyerMatchForm()

                return render(request, 'ezrego/buyavehicle.html', {'state0':1, 'form': form})

            elif request.POST['state'] == '1':
                form = BuyerCompletionForm(request.POST)
                uid = request.user.id
                u = Person.objects.get(user_auth_id=uid)
                if form.is_valid():
                    # Already a valid transfer code
                    valid_tcode = form.cleaned_data['transfer_code']
                    t = VehicleTransfer.objects.get(transfer_code=valid_tcode)
                    t.buyer = u
                    t.save()

                    s = Person.objects.get(id=t.seller.id)
                    return render(request, 'ezrego/buyavehicle.html', {'state2':1, 'transfer':t, 'seller':s})
                else:
                    return render(request, 'ezrego/buyavehicle.html', {'state1':1, 'form':form})

    form = BuyerMatchForm(initial={'state':'0'})
    return render(request, 'ezrego/buyavehicle.html', {'state0':1, 'form':form})

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
                username=p15,
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
