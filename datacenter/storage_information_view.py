from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from project.visits_analysis import get_duration, format_duration



def storage_information_view(request):
    non_closed_visits = []
    incomplete_visits = Visit.objects.filter(leaved_at=None)

    for incomplete_visit in incomplete_visits:
        entry_time = timezone.localtime(incomplete_visit.entered_at)
        employee_passcard = incomplete_visit.passcard
        employee_name = employee_passcard.owner_name
        duration = format_duration(get_duration(incomplete_visit))

        non_closed_visit = {
            'who_entered': employee_name,
            'entered_at': entry_time,
            'duration': duration,
        }

        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)
