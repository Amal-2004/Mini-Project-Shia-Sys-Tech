# Generated by Django 4.2.5 on 2023-10-07 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shia_app', '0012_alter_userprofile_email_alter_userprofile_emp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='emp_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image_base64',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='super_user',
            field=models.BooleanField(default=False),
        ),
    ]
