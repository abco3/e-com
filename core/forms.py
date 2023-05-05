from django import forms


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'ชื่อ',
        'class': 'form-control'
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'นามสกุล',
        'class': 'form-control'
    }))
    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': '08xxxxxxxx',
        'class': 'form-control'
    }))
    street_address = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': '1234 หมู่ x ถนน xxxx',
        'class': 'form-control'
    }))
    province = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'custom-select d-block w-100'
    }))
    zip = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': '1xxxx',
        'class': 'form-control'
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    # payment_option = forms.ChoiceField(
    #     widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
    reciept = forms.FileField(required=True)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()

    from django import forms
# from .models import MobilePhone

class MobilePhoneForm(forms.ModelForm):
    # class Meta:
    #     model = MobilePhone
    #     fields = ['model']
    #     widgets = {
    #         'model': forms.Select(attrs={'class': 'form-control'}),
    #     }
 model = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'ชื่อ',
        'class': 'form-control'
    }))