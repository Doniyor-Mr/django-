# Generated by Django 3.1.6 on 2021-02-12 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210213_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='kategoriya')),
            ],
            options={
                'verbose_name': 'kategoriya',
                'verbose_name_plural': 'kategoriylar',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['created_at'], 'verbose_name': 'habar', 'verbose_name_plural': 'habarlar'},
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category'),
        ),
    ]
