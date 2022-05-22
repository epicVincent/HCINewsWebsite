from django import forms
from subscribers.models import Subscriber,Recents
class Subscriberform(forms.Form):
    First_Name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Last_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Password = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    confirm_password=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))

class SubscriberClassForm(forms.ModelForm):
    class Meta():
        model = Subscriber
        fields = ('First_Name','Last_name','Email', 'is_admin')

        widgets = {
            'First_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_admin': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }