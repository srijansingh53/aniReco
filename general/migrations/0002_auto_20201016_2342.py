# Generated by Django 3.1 on 2020-10-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='anime_rank',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='anime_score',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='start_season',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='start_year',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='synopsis',
        ),
        migrations.AddField(
            model_name='anime',
            name='anime_premiered',
            field=models.CharField(default='Missing', max_length=10),
        ),
        migrations.AlterField(
            model_name='anime',
            name='anime_name',
            field=models.CharField(default='Missing', max_length=100),
        ),
        migrations.AlterField(
            model_name='anime',
            name='anime_rating',
            field=models.CharField(default='Missing', max_length=100),
        ),
        migrations.AlterField(
            model_name='anime',
            name='anime_synonyms',
            field=models.CharField(default='Missing', max_length=300),
        ),
        migrations.AlterField(
            model_name='anime',
            name='anime_type',
            field=models.CharField(default='Missing', max_length=50),
        ),
        migrations.AlterField(
            model_name='anime',
            name='duration_min',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='anime',
            name='genre',
            field=models.CharField(default='Missing', max_length=200),
        ),
        migrations.AlterField(
            model_name='anime',
            name='status',
            field=models.CharField(default='Missing', max_length=8),
        ),
        migrations.AlterField(
            model_name='anime',
            name='studio',
            field=models.CharField(default='Missing', max_length=200),
        ),
    ]
