# Generated by Django 3.1 on 2020-10-16 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_anime_anime_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='anime_rank',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=6),
        ),
    ]
