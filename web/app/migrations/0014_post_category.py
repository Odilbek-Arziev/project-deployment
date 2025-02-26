# Generated by Django 5.0.1 on 2024-04-18 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_comment_first_comment_alter_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('programming', 'Программирование'), ('it', 'IT'), ('design', 'Дизайн'), ('marketing', 'Маркетинг'), ('sport', 'Спорт'), ('politics', 'Политика'), ('other', 'Другое')], default='other', max_length=255),
        ),
    ]
