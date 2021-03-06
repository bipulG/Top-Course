# Generated by Django 3.0.5 on 2020-04-03 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Описание')),
                ('rate', models.IntegerField(verbose_name='Оценка')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('order_number', models.IntegerField(verbose_name='Порядковый номер')),
                ('link', models.TextField(verbose_name='Название')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
                'ordering': ['order_number'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('language', models.CharField(db_index=True, max_length=30, verbose_name='Язык')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Изменено')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('requirement', models.TextField(blank=True, null=True, verbose_name='Требование к курсу')),
                ('sale', models.IntegerField(default=0, verbose_name='Скидка в %')),
                ('feedback', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='top_course.Feedback', verbose_name='Отзывы')),
                ('videos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='top_course.Video', verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ['feedback__rate'],
            },
        ),
    ]
