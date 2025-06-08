from django.utils import timezone


ONE_HOUR = 3600
ONE_MINUTE = 60


def get_duration(visit):
    entry_time = timezone.localtime(visit.entered_at)
    exit_time = visit.leaved_at or timezone.localtime()

    return int((exit_time - entry_time).total_seconds())


def format_duration(duration):
    hours = duration // ONE_HOUR
    minutes = (duration % ONE_HOUR) // ONE_MINUTE
    seconds = duration % ONE_MINUTE

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


def is_visit_long(visit, minutes=60):
    duration_seconds = get_duration(visit)

    duration_minutes = duration_seconds / ONE_MINUTE

    return duration_minutes >= minutes