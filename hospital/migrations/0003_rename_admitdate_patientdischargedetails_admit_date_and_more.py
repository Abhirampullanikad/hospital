# Generated by Django 5.2.1 on 2025-05-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_appointment_patientdischargedetails_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientdischargedetails',
            old_name='admitDate',
            new_name='admit_date',
        ),
        migrations.AddField(
            model_name='patient',
            name='assignedDoctorId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/'),
        ),
    ]
