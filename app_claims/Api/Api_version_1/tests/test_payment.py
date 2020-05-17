# from django.test import TestCase, Client
# from django.urls import reverse
# import json
# from rest_framework import status
# from app_claims.Api.Api_version_1.serializers.payment_serializer import AcceptPaymentSerializer
# from app_claims.models import Batch, Payment

# # Initialize the APIClient app
# client = Client()

# class PaymentTest(TestCase):
#     """ Test module for Batch model """

#     def setUp(self):
#         self.new_batch = Batch.objects.create(
#             name = "test_batch",
#             batch_id = "test12345"
#         )

#         Payment.objects.create(
#             reason_approved_or_denied = "Above budget",
#             total_approved = "2000",
#             batch = self.new_batch,
#             date_created = "2020-01-26",
#             is_approved = "False"
            
#         )

#     def test_can_get_all_payment(self):
#         # get API response
#         response = client.get(reverse("app_claims:accept-payment-list"))
#         # get data from db
#         payments = Payment.objects.all()
#         serializer = AcceptPaymentSerializer(payments, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        

# # class GetSingleBatchTest(TestCase):
# #     def setUp(self):
# #         self.test_batch_one =  Batch.objects.create(
# #             batch_id = "futo12345",
# #             name = "FutoBatch",
# #         )
# #         self.test_batch_two = Batch.objects.create(
# #             batch_id = "August12345",
# #             name = "AugustBatch",
# #         )

# #     def test_get_valid_single_batch(self):
# #         response = client.get(reverse("app_claims:create-upload-detail", kwargs={'pk': self.test_batch_one.pk}))
# #         batch = Batch.objects.get(pk=self.test_batch_one.pk)
# #         serializer = BatchUploadSerializer(batch)
# #         self.assertEqual(response.data, serializer.data)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)

# #     def test_get_invalid_single_batch(self):
# #         response = client.get(
# #             reverse('app_claims:create-upload-detail', kwargs={'pk': 30})
# #         )
# #         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# # def CreateNewBatchTest(TestCase):
# #     """ Test module for inserting a new batch """
# #     def setUp(self):
# #         self.valid_payload = {
# #             'name': "October",
# #             'batch_id': "October12345"
# #         }
# #         self.invalid_payload = {
# #             'name' : "",
# #             'batch_id' : "test12345"
# #         }
# #     def test_create_valid_batch(self):
# #         response = client.post(
# #             reverse('app_claims:create-upload-list'),
# #             data=json.dumps(self.valid_payload),
# #             content_type='application/json'
# #         )
# #         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# #     def test_create_invalid_batch(self):
# #         response = client.post(
# #             reverse('app_claims:create-upload-list'),
# #             data=json.dumps(self.invalid_payload),
# #             content_type='application/json'
# #         )
# #         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# # # Test for API clients for deleting a batch
# # class DeleteSingleBatchTest(TestCase):
# #     """ Test module for deleting an existing puppy record """

# #     def setUp(self):
# #         self.new_batch = Batch.objects.create(
# #             name = "test_batch",
# #             batch_id = "test12345"
# #         )

# #     def test_valid_delete_batch(self):
# #         response = client.delete(
# #             reverse('app_claims:create-upload-detail', kwargs={'pk': self.new_batch.pk}))
# #         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# #     def test_invalid_delete_batch(self):
# #         response = client.delete(
# #             reverse('app_claims:create-upload-detail', kwargs={'pk': 30}))
# #         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)