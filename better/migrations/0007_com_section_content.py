# Generated by Django 4.0.6 on 2022-09-13 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('better', '0006_rename_post_com_section_grace'),
    ]

    operations = [
        migrations.CreateModel(
            name='com_section_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=300)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('joy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='better.content')),
            ],
            options={
                'ordering': ('time',),
            },
        ),
    ]
