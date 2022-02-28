# Generated by Django 2.2.8 on 2022-02-28 21:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('hknweb', '0001_initial'), ('hknweb', '0002_auto_20180401_1733'), ('hknweb', '0003_auto_20180406_2058'), ('hknweb', '0004_link'), ('hknweb', '0005_delete_link'), ('hknweb', '0006_profile_email'), ('hknweb', '0007_remove_profile_email'), ('hknweb', '0008_alumnus'), ('hknweb', '0009_delete_alumnus'), ('hknweb', '0010_announcement'), ('hknweb', '0011_reviewsession'), ('hknweb', '0012_delete_reviewsession'), ('hknweb', '0013_auto_20210202_0210')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=85)),
                ('text', models.TextField(blank=True, default='', max_length=2000)),
                ('visible', models.BooleanField(default=False)),
                ('release_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('private', models.BooleanField(default=True, verbose_name='Private profile?')),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must be ten digits.', regex='^([^\\d]*\\d){10}$')])),
                ('resume', models.FileField(blank=True, upload_to='')),
                ('graduation_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('candidate_semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hknweb.Semester')),
            ],
        ),
    ]
