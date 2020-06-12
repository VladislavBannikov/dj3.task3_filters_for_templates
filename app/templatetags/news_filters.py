from django import template
from datetime import datetime, timedelta

register = template.Library()


@register.filter
def format_date(value):
    dt_now = datetime.now()
    try:
        dt_value = datetime.fromtimestamp(value)
        dt_delta = dt_now - dt_value
        minutes_since = int(dt_delta.total_seconds() / 60)
        hours_since = int(minutes_since / 60)
        if hours_since > 24:
            return dt_value.strftime("%Y-%m-%d")
        elif hours_since:
            return f'{hours_since} часов назад'
        elif minutes_since > 10:
            return f'1 час назад'
        else:
            return "только что"
    except ValueError:
        return value


@register.filter
def format_score(value, default):
    if value is None:
        return default
    try:
        v = int(value)
    except ValueError:
        return value

    if v < -5:
        return "все плохо"
    elif -5 < v < 5:
        return "нейтрально"
    else:
        return "хорошо"


@register.filter
def format_num_comments(value):
    try:
        v = int(value)
    except ValueError:
        return value
    if v > 50:
        return "50+"
    elif 0 < v < 50:
        return value
    else:
        return "Оставьте комментирй"


@register.filter
def format_selftext(value, count=5):
    words = str(value).split()
    if words:
        return f'{" ".join(words[:count])} ... {" ".join(words[-count:])}'
    else:
        return ""