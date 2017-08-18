from django import forms
from catalogoapp.models.profile import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'role',
            'restaurant',
            'is_student',
        ]
        labels = {
            'role': 'Rol del usuario',
            'restaurant': 'Restaurante en que labora',
            'is_student': 'Es estudiante?'
        }
        widgets = {
            'role': forms.Select(attrs={'name': 'selectRole'}),
            'restaurant': forms.Select(attrs={'name': 'selecRestaurant'}),
            'is_student': forms.CheckboxInput(attrs={'name': 'checkIsStudent'}),
        }
