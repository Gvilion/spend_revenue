from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RevenueStatistic


@api_view(["GET"])
def revenue_statistics(request):
    revenue_data = RevenueStatistic.objects.values("date", "name").annotate(
        total_revenue=Sum("revenue"),
        total_spend=Sum("spend__spend"),
        total_impressions=Sum("spend__impressions"),
        total_clicks=Sum("spend__clicks"),
        total_conversion=Sum("spend__conversion")
    )

    revenue_list = list(revenue_data)

    return Response(revenue_list)

