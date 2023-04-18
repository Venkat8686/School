#pylint: disable=missing-module-docstring
#pylint: disable=missing-function-docstring
#pylint: disable=no-member
#pylint: disable=unused-argument
#pylint: disable=no-member
#pylint: disable=no-member

from .models import AcademicSession, AcademicTerm, SiteConfig


def site_defaults(request):
    current_session = AcademicSession.objects.get(current=True)
    current_term = AcademicTerm.objects.get(current=True)
    vals = SiteConfig.objects.all()
    contexts = {
        "current_session": current_session.name,
        "current_term": current_term.name,
    }
    for val in vals:
        contexts[val.key] = val.value

    return contexts
