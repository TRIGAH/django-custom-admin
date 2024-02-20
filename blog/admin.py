from django.contrib import admin
from .models import Post
# Register your models here.

class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin'


blog_site = BlogAdminArea(name='BlogAdmin')    
blog_site.register(Post)