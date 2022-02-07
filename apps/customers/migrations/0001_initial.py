# Generated by Django 4.0.2 on 2022-02-07 12:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import phonenumber_field.modelfields
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=250, verbose_name='UID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Patronymic')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('client_type', models.CharField(choices=[('primary', 'Primary'), ('repeated', 'Repeated'), ('external', 'External'), ('indirect', 'Indirect')], max_length=10, verbose_name='Client Type')),
                ('gender', models.CharField(choices=[('man', 'Man'), ('woman', 'Woman'), ('unknown', 'Unknown')], max_length=10, verbose_name='Gender')),
                ('timezone', timezone_field.fields.TimeZoneField(default='UTC', verbose_name='Timezone')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('status_change_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=250, verbose_name='UID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('client', models.ManyToManyField(related_name='departments', to='customers.Client', verbose_name='Client')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='customers.department', verbose_name='Parent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('vk', 'VK'), ('fb', 'FB'), ('ok', 'OK'), ('instagram', 'Instagram'), ('telegram', 'Telegram'), ('whatsapp', 'Whatsapp'), ('viber', 'Viber')], max_length=9)),
                ('link', models.CharField(max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_accounts', to='customers.client', verbose_name='Social Accounts')),
            ],
            options={
                'verbose_name': 'Social Account',
                'verbose_name_plural': 'Social Accounts',
                'db_table': 'client_social_accounts',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=250, verbose_name='UID')),
                ('name', models.CharField(max_length=150, verbose_name='Name organization')),
                ('short_name', models.CharField(max_length=10, verbose_name='Short Name organization')),
                ('tin', models.CharField(max_length=12, verbose_name='TIN')),
                ('ppc', models.CharField(max_length=9, verbose_name='Checkpoint')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('departments', models.ManyToManyField(blank=True, related_name='departments', to='customers.Department', verbose_name='Departments')),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
                'db_table': 'organizations',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='customers.client', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Client Email',
                'verbose_name_plural': 'Client Emails',
                'db_table': 'client_emails',
            },
        ),
        migrations.CreateModel(
            name='AdditionalPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_more', to='customers.client', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Client Phone',
                'verbose_name_plural': 'Client Phones',
                'db_table': 'client_phones',
            },
        ),
    ]
