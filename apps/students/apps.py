#pylint: disable=missing-module-docstring
#pylint: disable=missing-function-docstring
#pylint: disable=missing-module-docstring
#pylint: disable=missing-function-docstring
#pylint: disable=missing-class-docstring
#pylint: disable=unused-argument
#pylint: disable=unexpected-keyword-arg
#pylint: disable=arguments-differ
#pylint: disable=singleton-comparison
#pylint: disable=too-many-ancestors
#pylint: disable=no-member
#pylint: disable=too-few-public-methods
#pylint: disable=bad-option-value
#pylint: disable=missing-class-docstring
#pylint: disable=unused-import
#pylint: disable=import-outside-toplevel
from django.apps import AppConfig


class StudentsConfig(AppConfig):
    name = "apps.students"

    def ready(self):
        import apps.students.signals
