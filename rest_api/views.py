from rest_framework import generics, permissions
from .serializers import ImdbRatingModelSerializer, UserKpiDetailSerializer
from .models import ImdbRatingModel, UserKpiDetail
from django.contrib.auth.models import User
# import django_filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter

# from django_filters.rest_framework import DjangoFilterBackend


class CreateImdbRatingView(generics.ListCreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = ImdbRatingModel.objects.all()
    serializer_class = ImdbRatingModelSerializer
    permission_classes = (
        permissions.IsAuthenticated,)


class DetailsImdbRatingView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""

    queryset = ImdbRatingModel.objects.all()
    serializer_class = ImdbRatingModelSerializer
    permission_classes = (
        permissions.IsAuthenticated,)


# class ImdbRatingModelFilter(django_filters.FilterSet):
#     class Meta:
#         model = ImdbRatingModel
#         fields = ['id','popularity_99','director','genre','imdb_score','name']


class RetrieveImdbRatingView(generics.ListAPIView):
    """This class handles GET requests."""
    search_fields = ['id','popularity_99','director','genre','imdb_score','name']
    filter_backends = (SearchFilter,)
    queryset = ImdbRatingModel.objects.all()
    serializer_class = ImdbRatingModelSerializer
    pagination_class = PageNumberPagination
    # filter_class = ImdbRatingModelFilter
    # filter_fields = ('name')



class CreateUserKpiDetailView(generics.ListCreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = UserKpiDetail.objects.all()
    serializer_class = UserKpiDetailSerializer
    

class DetailUserKpiView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""

    queryset = UserKpiDetail.objects.all()
    serializer_class = UserKpiDetailSerializer
    