# Generated by Django 3.0.8 on 2020-11-24 12:14

#pylint: disable=missing-module-docstring
#pylint: disable=missing-function-docstring
#pylint: disable=unused-argument
#pylint: disable=unexpected-keyword-arg
#pylint: disable=arguments-differ
#pylint: disable=singleton-comparison
#pylint: disable=too-many-ancestors
#pylint: disable=missing-class-docstring
#pylint: disable=no-member
#pylint: disable=invalid-name
#pylint: disable=too-few-public-methods
#pylint: disable=bad-option-value
#pylint: disable=missing-class-docstring
#pylint: disable=unused-import

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0003_auto_20200726_0925"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academicsession",
            name="current",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="academicterm",
            name="current",
            field=models.BooleanField(default=True),
        ),
    ]
