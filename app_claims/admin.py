from django.contrib import admin
from .models import Claim, CareProvider, Batch,Payment,OutPatientConsultation, FamilyPlanning, Management


class ClaimAdmin(admin.ModelAdmin):  
    list_display = ['amount_claimed',
                    'amount_to_pay','amount_denied','completed', 'claim_batch']
    list_filter = ['completed', 'date_created',]
    search_fields = ['patient_complaints', 'claim_batch']
    list_per_page = 50

admin.site.register(Claim, ClaimAdmin)

admin.site.register(Management)
admin.site.register(OutPatientConsultation)
admin.site.register(FamilyPlanning)
class CareProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'lga', 'date_created']
    list_filter = ['name', 'lga', 'date_created']
    search_fields = ['name', 'lga', 'date_created']
    list_per_page = 50

admin.site.register(CareProvider, CareProviderAdmin)

class BatchAdmin(admin.ModelAdmin):
    list_display = ['name', 'batch_id', 'is_approved','date_created']
    list_filter = ['batch_id', 'is_approved', 'date_created',]
    search_fields = [ 'name', 'batch_id']
    list_per_page = 50
admin.site.register(Batch, BatchAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['batch', 'total_approved', 'is_approved', 'date_created']
    list_filter = ['batch', 'is_approved']
    search_fields = ['batch', 'reason_approved_or_denied', 'total_approved']
    list_per_page = 50

admin.site.register(Payment, PaymentAdmin)

