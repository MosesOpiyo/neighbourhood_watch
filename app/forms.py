from django.forms import ModelForm
from .models import Neighbourhood, User

class NeighbourForm(ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('name',)
class ProfileForm(ModelForm):
    class Meta:
        model = User   
        fields = ('profile_pic',)
        exclude = ('name','email','Neighbourhood_id')  

