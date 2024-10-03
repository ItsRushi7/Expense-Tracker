from django.contrib import admin

# Register your models here.

from Myapp.models import MyExpense

admin.site.register(MyExpense)
