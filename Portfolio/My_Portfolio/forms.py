from django import forms
from .models import *
from django.forms import ModelForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'message': '',
        }
        widgets = {
                'name': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder':'Name'}),
                'email':forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'Email'}),
                'subject': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder':'Subject'}),
                'message':forms.Textarea(attrs = {'class' : 'form-control', 'rows': '5', 'placeholder':'Message'}),
            }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        labels = {
            'course': '',
            'start_year': '',
            'end_year': '',
            'school': '',
            'city': '',
        }
        widgets = {
                'course': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Course'}),
                'start_year':forms.DateInput(attrs = {'class':'form-control mt-2', 'placeholder':'Start Year'}),
                'end_year': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'End Year'}),
                'school': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'School'}),
                'city': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'City'}),
            }

class TechnicalForm(forms.ModelForm):
    class Meta:
        model = Technical_Skills
        fields = '__all__'
        labels = {
            'skill': '',
        }
        widgets = {
                'skill': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Skill'}),
            }

# class SoftForm(forms.ModelForm):
#     class Meta:
#         model = Soft_Skills
#         fields = '__all__'
#         widgets = {
#                 'skill': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Skill...'}),
#             }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        labels = {
            'position': '',
            'start_year': '',
            'end_year': '',
            'company': '',
            'description': '',
            'city': '',
        }
        widgets = {
                'position': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Position'}),
                'start_year':forms.DateInput(attrs = {'class':'form-control mt-2', 'placeholder':'Start Year'}),
                'end_year': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'End Year'}),
                'company': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Company'}),
                'description':forms.Textarea(attrs = {'class' : 'form-control', 'rows': '3', 'placeholder':'Description'}),
                'city': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'City'}),
            }

class LangForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = '__all__'
        labels = {
            'language': '',
        }
        widgets = {
                'language': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Skill'}),
            }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'
        labels = {
            'name': '',
            'image': '',
            'about': '',
            'tag_line': '',
            'address': '',
            'city': '',
            'statement': '',
            'email': '',
            'facebook': '',
            'github': '',
            'instagram': '',
            'twitter': '',
            'contact': '',
        }
        widgets = {
                'name': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Name'}),
                'about': forms.Textarea(attrs = {'class' : 'form-control mt-2', 'rows': '3', 'placeholder':'About'}),
                'tag_line': forms.Textarea(attrs = {'class' : 'form-control mt-2', 'rows': '1', 'placeholder':'Tag Line'}),
                'statement': forms.Textarea(attrs = {'class' : 'form-control mt-2', 'rows': '1', 'placeholder':'Profile Statement'}),
                'address':forms.TextInput(attrs = {'class' : 'form-control', 'placeholder':'Address'}),
                'city': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'City'}),
                'email':forms.EmailInput(attrs = {'class' : 'form-control', 'placeholder':'Email'}),
                'facebook': forms.URLInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Facebook'}),
                'github': forms.URLInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Github'}),
                'instagram': forms.URLInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Instagram'}),
                'twitter': forms.URLInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Twitter'}),
                'contact': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Contact'}),
                'image':forms.FileInput(attrs = {'class':'mt-2'}),
            }
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
        labels = {
            'name': '',
            'image': '',
            'description': '',
        }

        widgets = {
                'name': forms.TextInput(attrs = {'class' : 'form-control mt-2', 'placeholder':'Name'}),
                'description': forms.Textarea(attrs = {'class' : 'form-control mt-2', 'rows': '5', 'placeholder':'Description'}),
                'image':forms.FileInput(attrs = {'class':' mt-2'}),
            }