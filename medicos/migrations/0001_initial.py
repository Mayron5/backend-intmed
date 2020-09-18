# Generated by Django 3.1.1 on 2020-09-18 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidade', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.IntegerField()),
                ('nome', models.CharField(max_length=150)),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicos.especialidade')),
            ],
        ),
    ]
