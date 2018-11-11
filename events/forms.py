from django import forms


class CreditCardField(forms.Form):
    cardNumber = forms.IntegerField()
    cardExpiry = forms.IntegerField()
    cardCVC = forms.IntegerField()
    amountDeposit = forms.DecimalField()


