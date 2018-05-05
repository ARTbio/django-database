from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
class StockForm(forms.Form):
    post_title = forms.CharField(help_text="Enter stock name")
