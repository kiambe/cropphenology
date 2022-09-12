from multiprocessing import Value
from django.contrib import admin

# Register your models here.

from .models import *



admin.site.register(County)
admin.site.register(SubCounty)
admin.site.register(Ward) 
admin.site.register(ValueChain) 
admin.site.register(ValuechainVariety) 
admin.site.register(CropCalendar) 

#@admin.site.register(PlantingDatePlanner) 
@admin.register(PlantingDatePlanner)
class plantingDateAdmin(admin.ModelAdmin):
  list_display = ('id', 'calendar',  'min_maturity_period')

@admin.register(PlantingDatePlannerC)
class plantingDateCAdmin(admin.ModelAdmin):
  list_display = ('id','county' , 'vc_variety',  'min_maturity_period')

