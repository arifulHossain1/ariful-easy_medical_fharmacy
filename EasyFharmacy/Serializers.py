from rest_framework import serializers

from EasyFharmacy.models import Company, CompanyBank, Medicine, MedicalDetails, Employee, EmployeeSalary, Customer, \
    Bill, CustomerRequest, CompanyAccount, EmployeeBank, BillDetails


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CompanyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = "__all__"

    #def to_representation(self, instance):
       # response = super().to_representation(instance)
        #response['company'] = CompanySerializer(instance.company_id).data
        #return response


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company_id).data
        return response


class MedicalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetails
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['medicine'] = MedicineSerializer(instance.medicine_id).data
        return response


class MedicalDetailsSerializerOnly(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetails
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSalary
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['employee'] = EmployeeSerializer(instance.employee_id).data
        return response


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomerSerializer(instance.customer_id).data
        return response


class BillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetails
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['bill'] = BillSerializer(instance.bill_id).data
        return response

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['medicine'] = MedicineSerializer(instance.medicine_id).data
        return response


class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = "__all__"


class CompanyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company_id).data
        return response


class EmployeeBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBank
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['employee'] = EmployeeSerializer(instance.employee_id).data
        return response
