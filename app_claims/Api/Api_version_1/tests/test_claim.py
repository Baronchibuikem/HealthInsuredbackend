from django.test import TestCase, Client
from django.urls import reverse
import json
from rest_framework import status
from app_claims.Api.Api_version_1.serializers.claim_serializer import ClaimsSerializer
from app_claims.models import Claim, Batch

# Initialize the APIClient app
client = Client()

class ClaimTest(TestCase):
    """ Test module for Claim model """

    def setUp(self):
        batch = Batch.objects.create(
            name = "test_batch",
            batch_id = "test12345"
        )
        Claim.objects.create(
            first_name = "John",
            last_name = "Doe",
            phone_number = '07037541482',
            caregiver_phone_number = "09090909089",
            claim_batch = batch
        )

    def test_can_get_all_Claim(self):
        """ used to test the api endpoint to get all claims """
        response = client.get(reverse("app_claims:Claim-list"))
        # get data from db
        claims = Claim.objects.all()
        serializer = ClaimsSerializer(claims, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

class GetSingleClaimTest(TestCase):
    def setUp(self):
        self.batch = Batch.objects.create(
            name = "test_batch",
            batch_id = "test12345"
        )
        self.test_claim_one =  Claim.objects.create(
            first_name = "John",
            last_name = "Doe",
            phone_number = '07037541482',
            caregiver_phone_number = "09090909089",
            claim_batch = self.batch
        )

    def test_get_valid_single_claim(self):
        response = client.get(reverse("app_claims:Claim-detail", kwargs={'pk': self.test_claim_one.pk}))
        claim = Claim.objects.get(pk=self.test_claim_one.pk)
        serializer = ClaimsSerializer(claim)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_Claim(self):
        response = client.get(
            reverse('app_claims:Claim-detail', kwargs={'pk': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


def CreateNewClaimTest(TestCase):
    """ Test module for inserting a new Claim """
    def setUp(self):
        self.batch = Batch.objects.create(
            name = "test_batch",
            batch_id = "test12345"
        )
        self.valid_payload = {
            first_name : "John",
            last_name : "Doe",
            phone_number : '07037541482',
            caregiver_phone_number : "09090909089",
            claim_batch: self.batch
        }
        self.invalid_payload = {
            first_name : "",
            last_name : "Doe",
            phone_number : '07037541482',
            caregiver_phone_number : "",
            claim_batch: ""
        }
    def test_create_valid_Claim(self):
        response = client.post(
            reverse('app_claims:Claim-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_Claim(self):
        response = client.post(
            reverse('app_claims:Claim-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# class updateSingleClaimTest(TestCase):
#     """Test module for updating an existing claim record"""
#     def setUp(self):
#         self.batch = Batch.objects.create(
#             name = "test_batch",
#             batch_id = "test12345"
#         )
#         self.new_claim = Claim.objects.create(
#             first_name = "John",
#             last_name = "Doe",
#             phone_number = '07037541482',
#             caregiver_phone_number = "09090909089",
#             claim_batch = self.batch
#         )
#         self.valid_payload = {
#             "first_name" : "John",
#             "last_name" : "Doe",
#             "phone_number" : '07037541482',
#             "caregiver_phone_number" : "09090909089",
#             # "claim_batch" : self.batch
#         }
#         self.invalid_payload = {
#             "first_name" : "Testing",
#             "last_name" : "Admin",
#             "phone_number" : '07037541482',
#             "caregiver_phone_number" : "09090909089",
#             "claim_batch" : self.batch
#         }

#     def test_valid_update_claim(self):
#         response = client.put(
#             reverse('app_claims:Claim-detail', kwargs={'pk': self.new_claim.pk}),
#             data = json.dumps(self.valid_payload),
#             content_type = "application/json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_invalid_update_claim(self):
#         response = client.put(
#             reverse('app_claims:Claim-detail', kwargs={'pk': self.new_claim.pk}),
#             data = json.dumps(self.invalid_payload),
#             content_type = "application/json"
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleBatchTest(TestCase):
    """ Test module for deleting an existing puppy record """

    def setUp(self):
        self.batch = Batch.objects.create(
            name = "test_batch",
            batch_id = "test12345"
        )
        self.new_claim = Claim.objects.create(
            first_name = "John",
            last_name = "Doe",
            phone_number = '07037541482',
            caregiver_phone_number = "09090909089",
            claim_batch = self.batch
        )
    def test_valid_delete_claim(self):
        response = client.delete(
            reverse('app_claims:Claim-detail', kwargs={'pk': self.new_claim.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_claim(self):
        response = client.delete(
            reverse('app_claims:Claim-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)