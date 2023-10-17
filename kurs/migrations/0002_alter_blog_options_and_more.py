# Generated by Django 4.2.6 on 2023-10-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kurs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"verbose_name": "Статья", "verbose_name_plural": "Статьи"},
        ),
        migrations.RenameField(
            model_name="blog",
            old_name="date_create",
            new_name="date_of_creation",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="body",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="is_published",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="view_count",
        ),
        migrations.AddField(
            model_name="blog",
            name="overview",
            field=models.TextField(
                blank=True, max_length=350, null=True, verbose_name="содержимое"
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="view_counter",
            field=models.IntegerField(default=0, verbose_name="кол-во просмотров"),
        ),
        migrations.AlterField(
            model_name="blog",
            name="preview",
            field=models.ImageField(
                blank=True,
                default="placeholder.png",
                null=True,
                upload_to="",
                verbose_name="изображение",
            ),
        ),
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=150, verbose_name="заголовок"),
        ),
    ]
