from django.contrib import admin
from django.contrib.auth import get_user_model
from authemail.admin import EmailUserAdmin

class MyUserAdmin(EmailUserAdmin):
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), MyUserAdmin)