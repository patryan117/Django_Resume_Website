from django.contrib import admin
from resumeApp.models import *

# admin fields
myModels = [Job, Education, GeneralInfo]
admin.site.register(myModels)
