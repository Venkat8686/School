# Generated by Django 3.0.7 on 2020-07-26 08:25

#pylint: disable=missing-module-docstring
#pylint: disable=missing-function-docstring
#pylint: disable=unused-argument
#pylint: disable=unexpected-keyword-arg
#pylint: disable=arguments-differ
#pylint: disable=singleton-comparison
#pylint: disable=too-many-ancestors
#pylint: disable=missing-class-docstring
#pylint: disable=no-member
#pylint: disable=too-few-public-methods
#pylint: disable=bad-option-value
#pylint: disable=invalid-name
#pylint: disable=missing-class-docstring
#pylint: disable=unused-import

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0002_auto_20200506_1520"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academicsession",
            name="current",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="academicterm",
            name="current",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
