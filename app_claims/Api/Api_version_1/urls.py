from django.urls import path
from app_claims.Api.Api_version_1.viewset.claims_view import ClaimView
from app_claims.Api.Api_version_1.viewset.payment_view import AcceptPaymentView, RejectPaymentView
from app_claims.Api.Api_version_1.viewset.careprovider_view import CareProviderView
from app_claims.Api.Api_version_1.viewset.batch_upload_view import BatchUpload
from app_claims.Api.Api_version_1.viewset.family_planning_view import FamilyPlanningView
from app_claims.Api.Api_version_1.viewset.outpatient_consultation_view import OutPatientConsultationView
from app_claims.Api.Api_version_1.viewset.management_view import ManagementView
from rest_framework import routers

app_name = "app_claims"

router = routers.DefaultRouter()

router.register('management', ManagementView)

router.register('family-planning', FamilyPlanningView)

router.register('consultation', OutPatientConsultationView)

# This endpoint is used to perform CRUD operation on CareProvider database
router.register('providers', CareProviderView, 'CareProvider')

# This endpoint is used to approve payment
router.register('accept-batch-payment', AcceptPaymentView, 'accept-payment')

# This endpoint is used to reject payment
router.register('reject-batch-payment', RejectPaymentView, 'reject-payment')

# This endpoint is used to perform CRUD operation on Claim database
router.register('claims', ClaimView, 'Claim')

# This endpoint is used to perform CRUD operation on Batch database
router.register('batches', BatchUpload,  basename="create-upload")

urlpatterns = router.urls
