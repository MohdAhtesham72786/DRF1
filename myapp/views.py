from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Coupon
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.filters import orderingFilter,searchFilter 
#from rest_framework.filters import SearchFilter
#from rest_framework.decorators import apiview
# Create your views here.

#@apiview
class Coupon1(APIView):
    def get(self, request, pk):
        if pk == 0 : 
            coupon_obj=Coupon.objects.values('id','code','description','amount','amount_type')
        else:           
            coupon_obj=Coupon.objects.filter(id=pk).values('id','code','description','amount','amount_type')
        return Response({'data': coupon_obj})

              
    def post(self, request, pk):
        code = request.data['code']
        description = request.data['description']
        amount = request.data['amount']
        amount_type = request.data['amount_type']
        coupon_obj = Coupon.objects.create(code=code,description=description,amount=amount,amount_type=amount_type)
        coupon_obj.save()
        return Response({'code':code,'description':description,'amount':amount,'amount_type':amount_type})
        
    def put(self, request, pk):
        code = request.data['code']
        description = request.data['description']
        amount = request.data['amount']
        amount_type = request.data['amount_type']
        updatedCuponCount= Coupon.objects.filter(id=pk).update(code=code,description=description,amount=amount,amount_type=amount_type)
        if updatedCuponCount > 0 :
            return Response({'code':code,'description':description,'amount':amount,'amount_type':amount_type})
        else:
            return Response('Unable to update', status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        code = request.data['code']
        description = request.data['description']
        amount = request.data['amount']
        amount_type = request.data['amount_type']
        updatedCuponCount = Coupon.objects.filter(id=pk).update(code=code,description=description,amount=amount,amount_type=amount_type)
        if updatedCuponCount > 0 :
            return Response({'description':description,'amount':amount,'amount_type':amount_type})
        else:
            return Response('Unable to update', status=status.HTTP_400_BAD_REQUEST)
        
        
        
    def delete(self, request, pk):
        coupon_obj = Coupon.objects.get(id=pk).delete()
        return Response({"data":coupon_obj})
       
    
        


