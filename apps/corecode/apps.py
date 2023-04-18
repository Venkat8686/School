#pylint: disable=missing-module-docstring
#pylint: disable=missing-class-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=unused-import
from django.apps import AppConfig


class CorecodeConfig(AppConfig):
    name = "apps.corecode"

    def ready(self):
        import apps.corecode.signals
