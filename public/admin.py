from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import OfficeData, WarrantyAgents, PublicUserData


#  if stacked inline used becomes listed
class WarrantyInLine(admin.TabularInline):
    model = WarrantyAgents
    extra = 1

class OfficeDataAdmin(admin.ModelAdmin):
    #  fieldsets define the field property when data is selected in admin
    #  classes:collpase hides the field by default
    fieldsets = [
                ('Product Info', {'fields': ['productName', 'quantity']}),
                ('ProductType', {'fields': ['product_type']}),
                ('Model Details', {'fields': ['modelNo', 'modelDate']}),
                ('Date Details', {'fields': ['boughtdate', 'warrantyTimeInMonth']}),
                ('Rate Details', {'fields': ['boughtprice', 'depreciationRate']}),
                ('State Evaluation Details', {'fields': ['previousEvaluationDate', 'toBeEvaluatedEveryMonth'], 'classes': ['collapse']}),
                ('Store Options', {'fields': ['leasable', 'canBeBought'], 'classes': ['collapse']}),
    ]
    #  extra lines to model adds choice field
    inlines = [WarrantyInLine]

    #  edits the list information where all questions are listed
    #  by default only the first element is displayed
    list_display = ('id', 'productName', 'modelNo')

    '''
    # adds filtering capacity on list view i.e sidebar
    list_filter = ['pub_date']
    '''

    #  adds search bar in listing page
    search_fields = ['modelNo', 'productName']


admin.site.register(OfficeData, OfficeDataAdmin)
admin.site.register(PublicUserData)
