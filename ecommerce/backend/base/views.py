from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products

# Here uses function based views, but look up class based views for real stuff!


@api_view(['GET'])
def getRoutes(request):
    routes = [
        "/api/products/",
        "/api/products/create/",
        "/api/products/upload/",
        "/api/products/<id>/reviews/",
        "/api/products/top/",
        "/api/products/<id>/",
        "/api/products/delete/<id>/",
        "/api/products/<update>/<id>/"
    ]
    return Response(routes, safe=False)


def getProducts(request):
    return Response(products, safe=False)
