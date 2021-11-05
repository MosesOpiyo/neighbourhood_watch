from django.db.models import fields
from django.forms import ModelForm
from .models import Neighbourhood, User, Business,Neighbourhood_events

class NeighbourForm(ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('name','location')
class ProfileForm(ModelForm):
    class Meta:
        model = User   
        fields = ('profile_pic',)
        exclude = ('name','email','Neighbourhood_id')  

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ('name','description')

class EventForm(ModelForm):
    class Meta:
        model = Neighbourhood_events
        fields = ('event',)
        exclude = ('person',)

