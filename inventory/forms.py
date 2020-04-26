from django import forms
from .models import *


class FaceMaskForm(forms.ModelForm):
    class Meta:
        model = FaceMasks
        fields = ('type', 'price', 'status', 'issues')


class SanitizerForm(forms.ModelForm):
    class Meta:
        model = Sanitizers
        fields = ('type', 'price', 'status', 'issues')


class FaceShieldForm(forms.ModelForm):
    class Meta:
        model = FaceShields
        fields = ('type', 'price', 'status', 'issues')