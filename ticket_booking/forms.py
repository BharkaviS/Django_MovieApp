from django import forms
from .models import MovieDetails

class MovieDetailForm(forms.ModelForm):
    class Meta:
        model =  MovieDetails
        fields = ['title','description','slug','show_timing1','show_timing2','price','Tickets_available','Tickets_booked','Tickets_totprice','image']
