from django.contrib import admin
from .form import *
from .models import *


# Register your models here.


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['nomProject', 'typeBien', 'Observatioin']
    form = StockCreateForm
    list_filter = ['nomProject', 'typeBien']
    search_fields = ['nomProject', 'typeBien']



admin.site.register(Project)
admin.site.register(Stock, StockCreateAdmin)
# admin.site.register(Category)
admin.site.register(AddTask)
admin.site.register(User)
# admin.site.register(Country)
# admin.site.register(State)
# admin.site.register(City)
admin.site.register(Person)
admin.site.register(Contacts)

# admin.site.register(StockHistory)
