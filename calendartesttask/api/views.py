"""api views module"""
import json
from operator import attrgetter
from django.http import HttpResponse
from db.models import Agreement

def get_data(request):
    """get data of calendar
    Returns:
        json --  get data like json
    """
    years = set()
    param_filter = {}
    rez = {}

    if request.GET.get('country') is not None:
        param_filter.update({'company__country_id__in': request.GET.get('country').split(',')})

    if request.GET.get('negotiator') is not None:
        param_filter.update({'negotiator_id__in': request.GET.get('negotiator').split(',')})

    if request.GET.get('company') is not None:
        param_filter.update({'company_id__in': request.GET.get('company').split(',')})

    try:
        all_agreement = Agreement.objects.filter(**param_filter)

    except Exception:
        return HttpResponse(status=404)

    for item in all_agreement:
        years.add(item.stop.year)

    for item in years:
        rez[item] = [0]*12

    for item in all_agreement:
        min_period = min(item.period.all(), key=attrgetter('stop'))
        rez[item.stop.year][min_period.stop.month-1] += 1

    return HttpResponse(json.dumps(rez), content_type='application/json')
    