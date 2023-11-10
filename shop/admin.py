from django.contrib import admin
from shop.models import Category, Course

admin.site.site_header = "Courses Admin"
admin.site.site_title = 'welcome'
admin.site.index_title = "welcome to courses admin area"
admin.site.register(Course)
admin.site.register(Category)
