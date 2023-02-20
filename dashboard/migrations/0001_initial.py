# Generated by Django 4.0.2 on 2022-02-27 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100000)),
                ('lastname', models.CharField(max_length=100000)),
                ('category', models.CharField(max_length=100000)),
                ('ocular_image', models.ImageField(blank=True, null=True, upload_to='xrays/')),
                ('note', models.TextField()),
                ('prediction', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
