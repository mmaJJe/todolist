# Generated by Django 3.1.3 on 2020-11-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20201109_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nextenrolltime',
            name='kind',
            field=models.CharField(choices=[('P', 'Past'), ('N', 'Now')], default='B', max_length=1),
        ),
    ]
