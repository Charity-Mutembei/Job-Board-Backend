from django.contrib import admin
from .models import Work, WorkLog, User, Folder, Document
# Register your models here.
# our models classes are; User, WorkLog, Work
admin.site.register(Work)
admin.site.register(WorkLog)
admin.site.register(Folder)
admin.site.register(Document)

