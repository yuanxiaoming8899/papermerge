# Generated by Django 3.1 on 2020-11-03 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0029_auto_20201023_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_special_id', models.CharField(max_length=50, null=True, unique=True)),
                ('base_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='app_0_document_related', related_query_name='app_0_documents', to='core.document')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]