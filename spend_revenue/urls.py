from django.contrib import admin
from django.urls import path

from revenue.views import revenue_statistics
from spend.views import spend_statistics

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/revenue/statistics/", revenue_statistics),
    path("api/spend/statistics/", spend_statistics),
]