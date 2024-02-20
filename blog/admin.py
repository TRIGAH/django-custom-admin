from django.contrib import admin

# Register your models here.

class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin'


blog_site = BlogAdminArea(name='BlogAdmin')    