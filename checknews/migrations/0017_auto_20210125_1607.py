# Generated by Django 3.1.3 on 2021-01-25 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checknews', '0016_auto_20210125_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authassistant',
            name='committeeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checknews.authcommittee', verbose_name='隸屬身份'),
        ),
    ]
