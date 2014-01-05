from django.contrib import admin
from micro.models import Account, Blog

# Register your models here.
class BlogInline(admin.StackedInline):
	"""docstring for ClassName"""
	model = Blog
	extra = 2
		
class AccountAdmin(admin.ModelAdmin):
	"""docstring for MicroAdmin"""
	fieldsets = [
		(None,			{'fields':['username']}),
		(None, 			{'fields':['password']}),
	]

	inlines = [BlogInline]
		
admin.site.register(Account, AccountAdmin)
