from _decimal import Decimal

from django.db.models import Sum
from django.db.models.functions import Coalesce
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SpendStatistic


@api_view(['GET'])
def spend_statistics(request):
    spend_data = SpendStatistic.objects.values('date', 'name').annotate(
        total_spend=Sum('spend'),
        total_impressions=Sum('impressions'),
        total_clicks=Sum('clicks'),
        total_conversion=Sum('conversion'),
        total_revenue=Sum('revenuestatistic__revenue'),
    ).annotate(
        total_revenue=Coalesce("total_revenue", Decimal(0)),
    )

    spend_list = list(spend_data)

    return Response(spend_list)
