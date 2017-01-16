from django.contrib import admin

# Register your models here.
from .models import Question, Choice


#  if stacked inline used becomes listed
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    #  fieldsets define the field property when data is selected in admin
    #  classes:collpase hides the field by default
    fieldsets = [
                (None, {'fields': ['question_text']}),
                ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #  extra lines to model adds choice field
    inlines = [ChoiceInLine]

    #  edits the list information where all questions are listed
    #  by default only the first element is displayed
    list_display = ('question_text', 'pub_date')

    # adds filtering capacity on list view i.e sidebar
    list_filter = ['pub_date']

    #  adds search bar in listing page
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
