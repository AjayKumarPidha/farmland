from django.contrib import admin
from farmland_app.models import *
# Register your models here.
############  User Model ############# 
class CustomuserAdmin(admin.ModelAdmin):
    list_display =('id', 'first_name', 'last_name','phone_number','email', 'is_admin','created_at')
    ordering = ['id']
    list_editable=('email',)
    list_per_page=4
    search_fields=("first_name",)
    list_filter=('first_name',)

admin.site.register(CustomUser,CustomuserAdmin)



######## Farmer Contact Us Model #########

class ContactUsModel(admin.ModelAdmin):
   list_display =('id', 'full_name','email_address', 'subject', 'message','created_at')
   ordering = ['-id']
   search_fields=("full_name",)

admin.site.register(FarmerContactUs,ContactUsModel)

######## Request An Estimate Model ##########

class EstimateModel(admin.ModelAdmin):
   list_display =('id', 'first_name','last_name', 'phone_number', 'service_type','massage')
   ordering = ['-id']
   search_fields=("first_name",)

admin.site.register(RequestAnEstimate,EstimateModel)
admin.site.register(ServiceType)

######### Frequently Ask Question Model ###########
@admin.register(AskQuestions)
class AskQuestionModel(admin.ModelAdmin):
   list_display = ('id','question')
   ordering = ['id']
   search_fields = ('question',)

# admin.site.register(AskQuestions,AskQuestionModel)
admin.site.register(AnswerList)

@admin.register(ServiceView)
class ServiceFreshModel(admin.ModelAdmin):
   list_display = ('id', 'headding','description','image')
   ordering = ['id']
   search_fields = ('headding',)

@admin.register(EmailSubscribers)
class EmailSubscribeModel(admin.ModelAdmin):
   list_display = ('id','email')
   ordering = ['id']
   search_fields = ('email',)


@admin.register(ProjectView)
class OurProjectModel(admin.ModelAdmin):
   list_display = ('id', 'headding', 'image')
   ordering = ['id']
   search_fields = ('headding',)

admin.site.register(ContactImage)


########## Explore Project Model ##########

@admin.register(ExploreProject)
class ExploreProjectAdmin(admin.ModelAdmin):
   list_display = ('id', 'headding', 'image')
   ordering = ['id']
   search_fields = ('headding',)

########## Completed Project Model ##########

@admin.register(CompletedProject)
class CompletedProjectAdmin(admin.ModelAdmin):
   list_display = ('id', 'headding', 'number')
   ordering = ['id']
   search_fields = ('headding',)


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
   list_display = ('id', 'headding', 'description', 'image')
   ordering = ['id']
   search_fields = ('headding',)
