from django.db import models
from django.utils import timezone
from libs.constants import constants_others
from libs.constants import constants_medical_conditions
from app_enrollment.models import PlanRegistration


class OutPatientConsultation(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class FamilyPlanning(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Management(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Batch(models.Model):
    is_approved = models.BooleanField(default=False)
    batch_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)
    created_by = models.CharField(max_length=50,)
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return "{}".format(self.name)


class CareProvider(models.Model):
    name = models.CharField(max_length=120)
    lga = models.CharField(max_length=70)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'


class Claim(models.Model):
    first_name = models.CharField(max_length=200,)
    last_name = models.CharField(max_length=200,)
    unique_id = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=timezone.now)
    phone_number = models.PositiveIntegerField()
    guardian_name = models.CharField(max_length=200,)
    gender = models.CharField(max_length=10, choices=constants_others.Gender)
    address = models.CharField(max_length=200)
    guardian_name = models.CharField(max_length=200,)
    patient_complaints = models.TextField()
    examination_findings = models.TextField()
    drugs_given = models.TextField()
    family_planning = models.TextField(blank=True)
    management = models.TextField(blank=True)
    out_patient_consultation = models.TextField(blank=True)
    amount_claimed = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    amount_to_pay = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    amount_denied = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    reason = models.TextField(null=True, blank=True,)
    completed = models.BooleanField(default=False)
    vetted = models.BooleanField(default=False)
    caregiver_surname = models.CharField(max_length=50)
    caregiver_firstname = models.CharField(max_length=50)
    caregiver_date_uploaded = models.DateField(default=timezone.now)
    caregiver_health_facility = models.CharField(max_length=2500)
    caregiver_phone_number = models.PositiveIntegerField()
    patient_guardian_signature = models.ImageField(
        upload_to="media", blank=True, null=True)
    claim_batch = models.ForeignKey(
        Batch, related_name="claims", on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Payment(models.Model):
    date_created = models.DateField(default=timezone.now)
    is_approved = models.BooleanField(default=False)
    batch = models.OneToOneField(Batch, on_delete=models.CASCADE)
    reason_approved_or_denied = models.TextField(null=True)
    total_approved = models.FloatField(null=True)
