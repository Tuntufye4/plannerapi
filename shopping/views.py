from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, F
from django.db.models.functions import ExtractMonth, ExtractYear

from .models import ShoppingItem
from .serializers import ShoppingSerializer


class ShoppingViewSet(viewsets.ModelViewSet):           
    queryset = ShoppingItem.objects.all().order_by('-created_at')
    serializer_class = ShoppingSerializer

    @action(detail=False, methods=['get'])   
    def monthly_total(self, request):
        """
        Get total shopping cost for a given month and year
        Example:
        /api/shopping/monthly_total/?month=3&year=2026
        """

        month = request.query_params.get('month')
        year = request.query_params.get('year')

        queryset = ShoppingItem.objects.all()   

        if month:
            queryset = queryset.annotate(
                month=ExtractMonth('created_at')
            ).filter(month=month)

        if year:   
            queryset = queryset.annotate(
                year=ExtractYear('created_at')
            ).filter(year=year)

        total = queryset.aggregate(
            total_cost=Sum(F('price') * F('quantity'))
        )['total_cost'] or 0

        return Response({
            "month": month,
            "year": year,
            "total_cost": total
        })                  