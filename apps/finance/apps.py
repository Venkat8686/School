#pylint: disable=unused-import
#pylint: disable=missing-class-docstring
#pylint: disable=import-outside-toplevel
#pylint: disable=missing-module-docstring
from django.apps import AppConfig


class FinanceConfig(AppConfig):
    name = "apps.finance"

    def ready(self):
        import apps.finance.signals
