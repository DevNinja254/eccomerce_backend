from django.contrib import admin
from .models import User, PaymentWaiting, Payment
from django.contrib.auth.admin import UserAdmin
from .forms import *
# Register your models here.
class Userdmin(admin.ModelAdmin):
    list_display = ["username", "email"]
    list_filter = ["username"]
    search_fields = ["username", "email"]

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone_number", "account_balance"]
    list_editable = ["phone_number"]
    search_fields = ["user"]


admin.site.register(User, Userdmin)
class CustomAdminUser(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
admin.site.register(PaymentWaiting)
admin.site.register(Payment)