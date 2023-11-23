from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# A way to add a choice box
payment_method = (
    ('Cash', 'Cash'),
    ('Transfer', 'Transfer'),
    ('Cheque', 'Cheque')
)

Projet_type = (
    ('Promotionnel', 'Promotionnel'),
    ('LOT Terrin', 'LOT Terrin'),
)

Bien_type = (
    ('Appartement F2', 'Appartement F2'),
    ('Appartement F3', 'Appartement F3'),
    ('Appartement F4', 'Appartement F4'),
    ('Appartement F5', 'Appartement F5'),
    ('Service', 'Service'),
    ('Local','Local')
)

Etat_Bien_Type = (
    ('Libre','Libre'),
    ('Réservé', 'Réservé'),
    ('Vendu','Vendu')
)

class Category(models.Model):
    group = models.CharField(max_length=50, blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.group)


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):             #acquereur
    nom = models.CharField(max_length=20)
    dateNaissance = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    lieuNaissance = models.CharField(max_length=150, blank=True, null=True,default="")
    phone= models.IntegerField() 
    email= models.CharField(max_length=20, blank=True, null=True,default="")
    idIdentite = models.IntegerField() 
    nomDossier = models.CharField(max_length=20, blank=True, null=True,default="")
    dateDossier = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    #affiche les biens dispo pour choisir
    def __str__(self):
        return str(self.nom)
    




class Project(models.Model):
    nom = models.CharField(max_length=150)
    type = models.CharField(choices=Projet_type, max_length=100)
    Localisation = models.CharField(max_length=150)
    nbrLotsTotal = models.IntegerField(default=0)    #nbr des logements(appartements et locaux et services) total dans le projet
    nbILOT = models.IntegerField()      #nbr des patiments total dans le projet
    Observation = models.TextField()


    def __str__(self):
        return f"{self.nom} - {self.type} - {self.Localisation}"
    

class Stock(models.Model):        #biens
    # nomProject = models.CharField(max_length=50, blank=True, null=True)  
    nomProject=models.ForeignKey(Project,on_delete=models.SET_NULL, blank=True, null=True)
    numLOT= models.CharField(max_length=50, blank=True, null=True)   #num batiment
    numBien=models.CharField(max_length=50, blank=True, null=True)    #num Porte
    bloc=models.CharField(max_length=50, blank=True, null=True)
    etage=models.CharField(max_length=50, blank=True, null=True)
    cote = models.CharField(max_length=50, blank=True, null=True)
    vue = models.CharField(max_length=50, blank=True, null=True)
    typeBien = models.CharField(choices=Bien_type, max_length=100)
    superficieHabitable = models.IntegerField(default='0', blank=True, null=True)
    superficieUtil= models.IntegerField(  blank=True, null=True)
    prixM2HorsTaxe = models.IntegerField(default='0', blank=True, null=True)
    prixM2TTC = models.IntegerField( blank=True, null=True)
    prixVenteM2 = models.IntegerField(  blank=True, null=True , default = 1)
    montantHorsTaxe = models.IntegerField(  blank=True, null=True)
    montantTTC = models.IntegerField()
    montantVenteTotal = models.IntegerField(  blank=True, null=True)  
    etat = models.CharField(choices=Etat_Bien_Type, max_length=100) 
    
    Observatioin = models.TextField()
    export_to_csv = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Bien"   
        verbose_name_plural = "Biens" 

    def __str__(self):
        return f"{self.nomProject} / LOT: {self.numLOT} /Num Bien: {self.numBien} --- --- --- {self.etat}"
    
    def save(self, *args, **kwargs):
        # Perform your calculations or custom logic here before saving
        # For example, let's say you want to double the quantity before saving
        self.montantVenteTotal  = self.prixVenteM2 * self.superficieHabitable
        self.montantHorsTaxe = self.prixM2HorsTaxe * self.superficieHabitable
        self.montantTTC = self.prixM2TTC * self.superficieHabitable


        # Call the save method of the parent class to actually save the instance
        super().save(*args, **kwargs)
    
    


class StockHistory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issued_by = models.CharField(max_length=50, blank=True, null=True)
    issued_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    re_order = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)







class Scrums(models.Model):
    task = models.CharField(max_length=100, blank=True, null=True)
    task_description = models.CharField(max_length=100, blank=True, null=True)
    task_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.task


class ScrumTitles(models.Model):
    lists = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.lists)


class Contacts(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=100, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='stock/static/images', null=True, blank=True)

    def __str__(self):
        return str(self.name)


class AddTask(models.Model):
    # user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Person, on_delete=models.CASCADE)
    product = models.ForeignKey(Stock, on_delete=models.CASCADE)
  
    total_amount=models.CharField(max_length=10000 ,default="")
    prixVenteM2 = models.IntegerField(  blank=True, null=True , default = 1)

    
    # phone_number = models.CharField(max_length=50, blank=True, null=True)
    deposit_amount=models.FloatField(max_length=950,  default= 0)
    payement_type = models.CharField(choices=payment_method, max_length=100)
    parts = models.IntegerField(default='0', blank=True, null=True)
    remaining_parts = models.IntegerField(default='0', blank=True, null=True)
    dateReservation= models.DateTimeField(auto_now_add=False, auto_now=False)
    NextdatePayement= models.DateTimeField(auto_now_add=False, auto_now=False,null=True,blank=True)

    confirmed=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.customer)
    
    class Meta:
        verbose_name = "Reservation"   
        verbose_name_plural = "Reservations"

    def save(self, *args, **kwargs):
        # Perform your calculations or custom logic here before saving
        # For example, let's say you want to double the quantity before saving
        self.total_amount  = self.product.montantVenteTotal
        self.product.prixVenteM2 = self.prixVenteM2
        # Call the save method of the parent class to actually save the instance
        super().save(*args, **kwargs)


class User(models.Model):
    user = models.TextField(default=None)

    def __str__(self):
        return self.user