# Generated by Django 4.2.4 on 2023-09-09 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sapp_hr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='award',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='award',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ceremony',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ceremony',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contract',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contract',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='deduction',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='deduction',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='department',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='department',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employeeaward',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employeeaward',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employeeskill',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employeeskill',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employeetarget',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employeetarget',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grade',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grade',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jobtype',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leave',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leave',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rank',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rank',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='remuneration',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='remuneration',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='settings',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='settings',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='skill',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='skill',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='target',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='target',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
    ]
