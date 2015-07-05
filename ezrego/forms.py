from django import forms

class PersonForm(forms.Form):
    personalorbusiness = forms.BooleanField(label="Personal or Company?", required=False, widget=forms.CheckboxInput())
    surname = forms.CharField(required=False)
    firstname = forms.CharField(required=False)
    companyname = forms.CharField(required=False)
    acn = forms.CharField(required=False)
    licencenumber = forms.CharField()
    dob = forms.DateField()
    homeaddress1 = forms.CharField()
    homeaddress2 = forms.CharField()
    homeaddresspostcode = forms.CharField()
    postaladdress1 = forms.CharField(required=False)
    postaladdress2 = forms.CharField(required=False)
    postaladdresspostcode = forms.CharField(required=False)
    phone = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

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
    transfer_code = forms.CharField()
    state = forms.CharField(widget=forms.HiddenInput())

class BuyerCompletionForm(forms.Form):
    garageaddress1 = forms.CharField()
    garageaddress2 = forms.CharField()
    garageaddresspostcode = forms.CharField()
    total_fee = forms.IntegerField()
    agreetoterms = forms.BooleanField(required=True)
    state = forms.CharField(widget=forms.HiddenInput())
    transfer_code = forms.CharField(widget=forms.HiddenInput())

