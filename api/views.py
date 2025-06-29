from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from students.models import Student
from .serializers import studentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from . serializers import employeeSerializer
from django.http import Http404
from rest_framework import mixins, generics,viewsets
from blogs.models import Blog, Comment
from blogs.serializers import blogSerializer, commentSerializer


@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        #Get all the data from the student table
        students = Student.objects.all()
        serializer = studentSerializer(students, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer= studentSerializer(student)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = studentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_200_OK)
    



# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = employeeSerializer(employees, many = True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = employeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

# class EmployeeDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
        
#         except Employee.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serailizer = employeeSerializer(employee)
#         return Response(serailizer.data, status= status.HTTP_200_OK)
    
#     def put(self,request,pk):
#        employee = self.get_object(pk)
#        serializer = employeeSerializer(employee, data = request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_200_OK)
#        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)


# Mixins uses 

# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = employeeSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    

# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = employeeSerializer


#     def get(self, request, pk):
#         return self.retrieve(request, pk)
    
#     def put(self, request, pk):
#         return self.update(request, pk)
    
#     def delete(self,request, pk):
#         return self.destroy(request, pk)
    

#Generic Views

# class Employees(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = employeeSerializer
# yesto satta ma autai ma combine wala use garna sakxam tala deko jastai 

# class Employees(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = employeeSerializer



# class EmployeeDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = employeeSerializer
#     lookup_field = 'pk'
#mathi 3 wata function ko lagi pharak pharak generics. garera import garna paryo tara sabai kam akkai chotti pani garna sakinxa tesko lagi pani function xa 

# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = employeeSerializer
#     lookup_field = 'pk'



# CRUD operation using viewsets 

# class EmployeeViewset(viewsets.ViewSet):
#     def list(self, reques):
#         queryset =Employee.objects.all()
#         serailizer = employeeSerializer(queryset, many = True)
#         return Response(serailizer.data, status= status.HTTP_200_OK)
    
#     def create(self, request):
#         serializer = employeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
#     def retrieve(self, request, pk = None):
#         employee = get_object_or_404(Employee, pk = pk)
#         serializer = employeeSerializer(employee)
#         return Response(serializer.data, status= status.HTTP_200_OK)
    
#     def update(self, request, pk =None):
#         employee = get_object_or_404(Employee, pk = pk)
#         serializer = employeeSerializer(employee, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_200_OK)
#         return Response(serializer.errors)
    
#     def delete(self, request, pk = None):
#         employee = get_object_or_404(Employee, pk = pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#using viewset.modelviewset


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer


class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer


class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer
    lookup_field = 'pk'


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentSerializer
    lookup_field = 'pk'


