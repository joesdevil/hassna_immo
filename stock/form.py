from django import forms
from .models import *


# fields = '__all__' to display all


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['group']





class AddProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["nom","type","nbrLotsTotal","Localisation", "nbILOT", "Observation" ]

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['nomProject','numLOT','numBien','bloc','etage','cote','vue','typeBien','superficieHabitable','superficieUtil','prixM2HorsTaxe','prixM2TTC','prixVenteM2','montantHorsTaxe','montantTTC','montantVenteTotal','etat','Observatioin']

    # def clean_category(self):
    #     category = self.cleaned_data.get('category')
    #     if not category:
    #         raise forms.ValidationError('This Field should not be empty')
    #     for something in Stock.objects.all():
    #         if something.category == category:
    #             raise forms.ValidationError(category + " Already Exists")
    #     return category
    #
    # def clean_item(self):
    #     item = self.cleaned_data.get('item_name')
    #     if not item:
    #         raise forms.ValidationError('This Field should not be empty')
    #     for something in Stock.objects.all():
    #         if something.category == item:
    #             raise forms.ValidationError(item + " Already Exists")
    #     return item


class StockHistorySearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)

    class Meta:
        model = StockHistory
        fields = ['category', 'item_name', 'start_date', 'end_date']


class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = Stock
        fields = ['typeBien','etat']

        

class DepSearchForm(forms.Form):
    
    # user = forms.CharField(required=False)
    export_to_CSV = forms.BooleanField(required=False)
         


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =["nom","type","nbrLotsTotal","Localisation", "nbILOT", "Observation" ]
        


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['nomProject','numLOT','numBien','bloc','etage','cote','vue','typeBien','superficieHabitable','superficieUtil','prixM2HorsTaxe','prixM2TTC','prixVenteM2','montantHorsTaxe','montantTTC','montantVenteTotal','etat','Observatioin']

        
    
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = '__all__'


class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['nomProject','numLOT','numBien','bloc','etage','cote','vue','typeBien','superficieHabitable','superficieUtil','prixM2HorsTaxe','prixM2TTC','prixVenteM2','montantHorsTaxe','montantTTC','montantVenteTotal','etat','Observatioin']



class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['nomProject','numLOT','numBien','bloc','etage','cote','vue','typeBien','superficieHabitable','superficieUtil','prixM2HorsTaxe','prixM2TTC','prixVenteM2','montantHorsTaxe','montantTTC','montantVenteTotal','etat','Observatioin']



class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['nomProject','numLOT','numBien','bloc','etage','cote','vue','typeBien','superficieHabitable','superficieUtil','prixM2HorsTaxe','prixM2TTC','prixVenteM2','montantHorsTaxe','montantTTC','montantVenteTotal','etat','Observatioin']


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = ['customer','product' ,"total_amount",'dateReservation',"payement_type","parts",'NextdatePayement',"deposit_amount" ]


class AddCountry(forms.ModelForm):
    class Meta:
        model = Country
        fields =  ['name']
        
        
class AddState(forms.ModelForm):
    class Meta:
        model = State
        fields =  ['name']
        
class AddCity(forms.ModelForm):
    class Meta:
        model = City
        fields =  ['name']



class DependentDropdownForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['nom','dateNaissance','lieuNaissance','phone','email','idIdentite','nomDossier','dateDossier','idBienDemande']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['state'].queryset = State.objects.none()
        # if 'country' in self.data:
        #     try:
        #         country_idm = int(self.data.get('country'))
        #         self.fields['state'].queryset = State.objects.filter(country_id=country_idm).order_by('name')
        #     except(ValueError, TypeError):
        #         pass
        # elif self.instance.pk:
        #     self.fields['state'].queryset = self.instance.country.state_set.order_by('name')

        # self.fields['city'].queryset = City.objects.none()
        # if 'state' in self.data:
        #     try:
        #         state_idm = int(self.data.get('state'))
        #         self.fields['city'].queryset = City.objects.filter(state_id=state_idm).order_by('name')
        #     except(ValueError, TypeError):
        #         pass
        # elif self.instance.pk:
        #     self.fields['city'].queryset = self.instance.state.city_set.order_by('name')


class AddScrumListForm(forms.ModelForm):
    class Meta:

        model = ScrumTitles
        fields = ['lists']


class AddScrumTaskForm(forms.ModelForm):
    class Meta:
        model = Scrums
        fields = ['task', 'task_description', 'task_date']


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
