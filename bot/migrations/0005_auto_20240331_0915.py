# Generated by Django 3.1.7 on 2024-03-31 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_prompt_chathistorybackup_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chathistory',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='chathistorybackup',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='prompt',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
