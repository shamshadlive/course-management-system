# Generated by Django 4.2.6 on 2023-10-12 07:31

from django.db import migrations, models
import django_summernote.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortTermCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('description', django_summernote.fields.SummernoteTextField()),
                ('course_img', models.ImageField(blank=True, null=True, upload_to='course/main_img/')),
                ('amount', models.IntegerField()),
                ('amount_in_text', models.CharField(max_length=200)),
                ('course_status', models.CharField(choices=[('EB', 'Enable'), ('DB', 'Disable')], default='DB', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
