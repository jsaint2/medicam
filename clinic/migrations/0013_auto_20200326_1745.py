# Generated by Django 3.0.4 on 2020-03-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0012_auto_20200326_0616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'provider'},
        ),
        migrations.AlterField(
            model_name='disclaimer',
            name='html',
            field=models.TextField(verbose_name='HTML'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='fcm_token',
            field=models.TextField(blank=True, null=True, verbose_name='FCM push token'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IP address'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=70, verbose_name='full name'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='notify',
            field=models.BooleanField(default=True, verbose_name='send notifications'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='utc_offset',
            field=models.IntegerField(default=0, verbose_name='UTC offset'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='verified',
            field=models.BooleanField(default=False, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IP address'),
        ),
    ]
