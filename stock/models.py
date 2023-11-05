from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# A way to add a choice box
payment_method = (
    ('Cash', 'Cash'),
    ('Transfer', 'Transfer'),
    ('Cheque', 'Cheque')
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


class Person(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone= models.CharField(max_length=20, blank=True, null=True)
    email= models.CharField(max_length=20, blank=True, null=True,default="")
    def __str__(self):
        return str(self.name)



class Project(models.Model):
    
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    start_date=models.DateTimeField(auto_now_add=False, auto_now=False)
    end_date=models.DateTimeField(auto_now_add=False, auto_now=False)


    def __str__(self):
        return str(self.name)
    

class Stock(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    block=models.CharField(max_length=50, blank=True, null=True)
    etage=models.CharField(max_length=50, blank=True, null=True)
    apartement=models.CharField(max_length=50, blank=True, null=True)
    Code_Bar = models.CharField(max_length=150, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issued_by = models.CharField(max_length=50, blank=True, null=True)
    issued_to = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(max_length=10000)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    re_order = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    date = models.DateTimeField(auto_now_add=False, auto_now=False)
    export_to_csv = models.BooleanField(default=False)
    image = models.ImageField(upload_to='stock/static/images', null=True, blank=True)

    def __str__(self):
        return self.item_name


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
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Person, on_delete=models.CASCADE)
    product = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
  
    total_amount=models.CharField(max_length=10000)
    
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    deposit_amount=models.FloatField(max_length=950,  default= 0)
    payement_type = models.CharField(choices=payment_method, max_length=100)
    parts = models.IntegerField(default='0', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=False, auto_now=False )
    confirmed=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.customer)



class User(models.Model):
    user = models.TextField(default=None)

    def __str__(self):
        return self.user