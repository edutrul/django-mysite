from polls.models import Poll, Choice
from django.contrib import admin

# admin.site.register(Poll)

class ChoiceInline(admin.TabularInline):
    """ ChoiceInLine class """
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    """ Changes for Admin Poll """
    #fields = ['pub_date', 'question']
    fieldsets = [
        (
            None, {
                'fields': ['question']
            }
        ),
        (
            'Date information', {
                'fields': ['pub_date'],
                'classes': ['collapse']
            }
        ),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
  
admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)
