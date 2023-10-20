from django.contrib import admin
from .models import Department, Course, Purpose, Customer, Material

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Purpose)
admin.site.register(Customer)
admin.site.register(Material)

