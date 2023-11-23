from django.shortcuts import render
# API ==> CREATED API BY " VIEWSET "
from rest_framework import viewsets
from myapi.models import Company ,Employee                                             # import models
from myapi.API.serializers import CompanySerializer,EmployeeSerializer                 # import serializer

# API particular by id
from rest_framework.decorators import action
from rest_framework.response import Response

#>==> API session Authentication <===<
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly



# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes =[SessionAuthentication]
    permission_classes =[IsAuthenticatedOrReadOnly]


   #companies/{companyId}/emplyees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):   
        try:                
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists !! Error'
            })



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


