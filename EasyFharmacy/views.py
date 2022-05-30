from django.shortcuts import render
from rest_framework import viewsets, generics
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from EasyFharmacy.Serializers import CompanySerializer, CompanyBankSerializer, MedicineSerializer, EmployeeSerializer, \
    EmployeeSalarySerializer, CustomerSerializer, MedicalDetailsSerializer, MedicalDetailsSerializerOnly
from EasyFharmacy.models import Company, CompanyBank, Medicine, Employee, EmployeeSalary, Customer, MedicalDetails


class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = Company.object.all()
        serializer = CompanySerializer(company, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Company List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CompanySerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "Company Data Save Successfully"}
        except:
            response_dict = {"error": True, "message": "Error While Saving Company Data"}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Company.object.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(company, context={"request": request})
        serializer_data=serializer.data
        company_bank_details = CompanyBank.object.filter(company_id=serializer_data["Id"])
        companybank_details_serializer = CompanyBankSerializer(company_bank_details, many=True)
        serializer_data["company_bank"] = companybank_details_serializer.data

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = Company.object.all()
            company = get_object_or_404(queryset, pk=pk)
            serilizer = CompanySerializer(company, data=request.data, context={"request": request})
            serilizer.is_valid(raise_exception=True)
            serilizer.save()
            response_dict = {"error": False, "message": "Company Data Successfully Updated"}
        except:
            response_dict = {"error": True, "message": "Error While Updating Company Data"}
        return Response(response_dict)


class CompanyBankViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        companybank = CompanyBank.object.all()
        serializer = CompanyBankSerializer(companybank, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Company Bank List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CompanyBankSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "Company Bank Data Save Successfully"}
        except:
            response_dict = {"error": True, "message": "Error While Saving Company Bank Data"}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = CompanyBank.object.all()
        companybank = get_object_or_404(queryset, pk=pk)
        serializer = CompanyBankSerializer(companybank, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = CompanyBank.object.all()
            companybank = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSerializer(companybank, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "Company Bank Data Successfully Updated"}
        except:
            response_dict = {"error": True, "message": "Error While Updating Company Bank Data"}
        return Response(response_dict)


class CompanyNameViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return Company.object.filter(name=name)

class CompanyonlyViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer
    def get_queryset(self):
        return Company.object.all()


class MedicineViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        medicine = Medicine.object.all()
        serializer = MedicineSerializer(medicine, many=True, context={"request": request})

        medicine_data=serializer.data
        medicinelist2=[]

        #Adding Extra Key for Medicine Details in Medicine
        for medicine in medicine_data:
            medicine_details=MedicalDetails.object.filter(medicine_id=medicine["Id"])
            medicine_details_serializer=MedicalDetailsSerializerOnly(medicine_details,many=True)
            medicine["medicine_details"]=medicine_details_serializer.data
            medicinelist2.append(medicine)

        response_dict = {"error": False, "message": "All Medicine related  Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = MedicineSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()

            medicine_id=serializer.data['Id']
            #print(medicine_id)

            medicine_details_list=[]
            for medicine_detail in request.data["medicine_details"]:
                #print(medicine_detail)
                medicine_detail["medicine_id"]=medicine_id
                medicine_details_list.append(medicine_detail)
                #print(medicine_details_list)

            serializer_2=MedicalDetailsSerializer(data=medicine_details_list,many=True,context={"request":request})
            serializer_2.is_valid()
            serializer_2.save()

            response_dict = {"error": False, "message": "Medicine Data Save Successfully"}
        except:
            response_dict = {"error": True, "message": "Error While Saving Medicine Data"}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Medicine.object.all()
        medicine = get_object_or_404(queryset, pk=pk)
        serializer = MedicineSerializer(medicine, context={"request": request})
        serializer_data=serializer.data
        medicine_details = MedicalDetails.object.filter(medicine_id=serializer_data["Id"])
        medicine_details_serializer = MedicalDetailsSerializerOnly(medicine_details, many=True)
        serializer_data["medicine_details"] = medicine_details_serializer.data

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def update(self, request, pk=None):
        try:
            queryset = Medicine.object.all()
            medicine = get_object_or_404(queryset, pk=pk)
            serializer = MedicineSerializer(medicine, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            for salt_detail in request.data["medicine_details"]:
                if salt_detail["Id"]==0:
                    del salt_detail["Id"]
                    salt_detail["medicine_id"]=serializer.data["Id"]
                    serializer_2 = MedicalDetailsSerializer(data=salt_detail,
                                                            context={"request": request})
                    serializer_2.is_valid()
                    serializer_2.save()

                else:
                    queryset2=MedicalDetails.object.all()
                    medicine_salt=get_object_or_404(queryset2,pk=salt_detail["Id"])
                    del salt_detail["Id"]
                    serializer3=MedicalDetailsSerializer(medicine_salt,data=salt_detail,context={"request":request})
                    serializer3.is_valid()
                    serializer3.save()
            response_dict = {"error": False, "message": "Medicine Data Successfully Updated"}
        except:
            response_dict = {"error": True, "message": "Error While Updating Medicine Data"}
        return Response(response_dict)


class EmployeeViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        employee = Employee.object.all()
        serializer = EmployeeSerializer(employee, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Employee List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "Employee Data Save Successfully"}
        except:
            response_dict = {"error": True, "message": "Error While Saving Employee Data"}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = Employee.object.all()
            employee = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "Employee Data Successfully Updated"}
        except:
            response_dict = {"error": True, "message": "Error While Updating Employee Data"}
        return Response(response_dict)


class EmployeeSalaryViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        employeesalary = EmployeeSalary.object.all()
        serializer = EmployeeSalarySerializer(employeesalary, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All EmployeeSalary List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = EmployeeSalarySerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "EmployeeSalary Data Save Successfully"}
        except:
            response_dict = {"error": True, "message": "Error While Saving EmployeeSalary Data"}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = EmployeeSalary.object.all()
        employeesalary = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSalarySerializer(employeesalary, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = EmployeeSalary.object.all()
            employeesalary = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSalarySerializer(employeesalary, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "EmployeeSalary Data Successfully Updated"}
        except:
            response_dict = {"error": True, "message": "Error While Updating EmployeeSalary Data"}
        return Response(response_dict)


class CustomerViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        customer = Customer.object.all()
        serializer = CustomerSerializer(customer, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Customer wise listed Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CustomerSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "Customer Data Save Successfully"}
        except:
            response_dict = {"error": True, "message": "Error While Saving Customer Data"}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = Customer.object.all()
            customer = get_object_or_404(queryset, pk=pk)
            serializer = CustomerSerializer(customer, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False, "message": "Customer Data Successfully Updated"}
        except:
            response_dict = {"error": True, "message": "Error While Updating Customer Data"}
        return Response(response_dict)


company_list = CompanyViewSet.as_view({"get": "list"})
company_create = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put": "update"})
