# Generated by Django 2.2.7 on 2020-02-07 11:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_approved', models.BooleanField(default=False)),
                ('batch_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created_by', models.CharField(max_length=50)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CareProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('lga', models.CharField(max_length=70)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyPlanning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OutPatientConsultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('is_approved', models.BooleanField(default=False)),
                ('reason_approved_or_denied', models.TextField(null=True)),
                ('total_approved', models.FloatField(null=True)),
                ('batch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_claims.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('unique_id', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('phone_number', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('guardian_name', models.CharField(max_length=200)),
                ('patient_complaints', models.TextField()),
                ('examination_findings', models.TextField()),
                ('drugs_given', models.TextField()),
                ('family_planning', models.TextField(blank=True)),
                ('management', models.TextField(blank=True)),
                ('out_patient_consultation', models.TextField(blank=True)),
                ('amount_claimed', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('amount_to_pay', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('amount_denied', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('vetted', models.BooleanField(default=False)),
                ('caregiver_surname', models.CharField(max_length=50)),
                ('caregiver_firstname', models.CharField(max_length=50)),
                ('caregiver_date_uploaded', models.DateField(default=django.utils.timezone.now)),
                ('caregiver_health_facility', models.CharField(max_length=2500)),
                ('caregiver_phone_number', models.PositiveIntegerField()),
                ('patient_guardian_signature', models.ImageField(blank=True, null=True, upload_to='media')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('claim_batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='app_claims.Batch')),
            ],
        ),
    ]
