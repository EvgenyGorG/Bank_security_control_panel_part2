from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration, format_duration
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    non_closed_visits = []
    people_in_the_vault = Visit.objects.filter(leaved_at=None)

    for human_in_the_vault in people_in_the_vault:
        entry_time = timezone.localtime(human_in_the_vault.entered_at)
        employee_passcard = human_in_the_vault.passcard
        employee_name = employee_passcard.owner_name
        duration = format_duration(get_duration(human_in_the_vault))

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
