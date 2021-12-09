# Generated by Django 3.2.9 on 2021-12-09 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amigos_app', '0002_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='name_friend',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='name_friend', to='amigos_app.user1'),
            preserve_default=False,
        ),
    ]
