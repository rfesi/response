# Generated by Django 2.2.3 on 2019-11-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("response", "0012_commschannel_onetoone")]

    operations = [
        migrations.AddField(
            model_name="incident",
            name="private",
            field=models.BooleanField(default=False),
        )
    ]
