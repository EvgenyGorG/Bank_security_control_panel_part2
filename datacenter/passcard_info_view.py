from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from project.visits_analysis import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        duration = get_duration(visit)
        duration = format_duration(duration)

        this_passcard_visit = {
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': is_visit_long(visit)
        }

        this_passcard_visits.append(this_passcard_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)
