from django import forms
from app.models import School, Study

class StudyForm(forms.ModelForm):
    #school_name = forms.CharField(label="Nom", widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom établissement'}))
    #code = forms.CharField(label='Code', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Code établissement'}))
    #boite_postal = forms.CharField(label='BP', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'BP établissement'}))
    class Meta:
        model = Study
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre nom'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre prenom'}),
            'serial_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre matricule'}),
            #'school': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre établissement'}),
            'label': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom établissement'}),
            'code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Code établissement'}),
            'post_box': forms.TextInput(attrs={'class':'form-control', 'placeholder':'BP établissement'})
        }
        labels = {
            'first_name': 'Nom',
            'last_name': 'Prenom',
            'serial_number':'Matricule',
            #'school': 'Établissement',
            'label': 'Etablissement',
            'code': 'Code',
            'post_box': 'Boite postale'
        }

    def clean_serial_number(self):
        serial_number = self.cleaned_data['serial_number']
        if Study.objects.filter(serial_number=serial_number):
            self.add_error('serial_number', 'Le matricule doit être unique')
        return serial_number
    #def save(self)