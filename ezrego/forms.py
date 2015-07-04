from django import forms

class PersonForm(forms.Form):
    personalorbusiness = forms.BooleanField(label="Personal or Company?", required=False, widget=forms.CheckboxInput())
    surname = forms.CharField()
    firstname = forms.CharField()
    companyname = forms.CharField()
    acn = forms.CharField()
    licencenumber = forms.CharField()
    dob = forms.DateField()
    homeaddress1 = forms.CharField()
    homeaddress1 = forms.CharField()
    homeaddresspostcode = forms.IntegerField()
    postaladdress1 = forms.CharField()
    postaladdress2 = forms.CharField()
    postaladdresspostcode = forms.IntegerField()
    phone = forms.IntegerField()
    email = forms.EmailField()

class SellerForm(forms.Form):
    current_rego = forms.CharField()
    rego_expiry = forms.DateField()
    vehicle_year = forms.IntegerField()
    vehicle_make = forms.CharField()
    vehicle_model = forms.CharField()
    vehicle_bodytype = forms.CharField()
    vehicle_vin = forms.CharField()
    is_pre1989 = forms.BooleanField(label="Vehicle is pre 1989?", required=False, widget=forms.CheckboxInput())
    is_written_off = forms.BooleanField(label="Vehicle is on written-off register?", required=False)
    is_rwc_attached = forms.BooleanField(label="RWC is attached?")
    rwc_serialnumber = forms.CharField()
    rwc_issuedate = forms.DateField()
    rwc_testerlicence = forms.CharField()
    market_value = forms.IntegerField()
    date_of_sale = forms.DateField()
    transfer_fee = forms.IntegerField()
    duty_fee = forms.IntegerField()
    agreetoterms = forms.BooleanField(required=True)

class BuyerMatchForm(forms.Form):
    transfercode = forms.CharField()

class BuyerCompletionForm(forms.Form):
    garageaddress1 = forms.CharField()
    garageaddress2 = forms.CharField()
    garageaddresspostcode = forms.IntegerField()
    total_fee = forms.IntegerField()
    agreetoterms = forms.BooleanField(required=True)

