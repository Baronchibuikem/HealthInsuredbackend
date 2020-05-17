from django.contrib import admin
from app_enrollment.models import Staff, Department, GenericPlan, Dependent, PlanRegistration, CustomUser


admin.site.register(GenericPlan)


admin.site.register(PlanRegistration)

admin.site.register(CustomUser)

class StaffAdmin(admin.ModelAdmin):  
    list_display = ['department',]
    list_filter = ['department',]
    search_fields = ['name',]
    list_per_page = 50

admin.site.register(Staff, StaffAdmin)


class DepartmentAdmin(admin.ModelAdmin):  
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name',]
    list_per_page = 50

admin.site.register(Department, DepartmentAdmin)


class DependentAdmin(admin.ModelAdmin):
    list_display = ['enrollee_id', 'email', 'phone',
                    'gender', 'genotype', 'blood_group',]
    list_filter = ['gender', 'genotype', ]
    search_fields = [ 'email', 'phone', 'state', 'address']
    list_per_page =50
    
admin.site.register(Dependent, DependentAdmin)
