from django import forms


class MatchBetForm(forms.Form):
    moneyBet = forms.DecimalField()
    typeBet = forms.CharField()


class CreditCardField(forms.Form):
    cardNumber = forms.IntegerField()
    cardExpiry = forms.IntegerField()
    cardCVC = forms.IntegerField()
    amountDeposit = forms.DecimalField()


