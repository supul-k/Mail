# Generated by Django 4.2.1 on 2023-05-18 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_email_spam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='attachments',
        ),
    ]