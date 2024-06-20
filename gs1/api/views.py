from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#model - student object data
def student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')
    # return JsonResponse(serializer.data)

#queryset all students data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many = True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type = 'application/json')
    #here data is not in dict format hence we have to put safe as false to accept all type of data
    return JsonResponse(serializer.data,safe= False)

@csrf_exempt
def create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythod_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythod_data)
        if serializer.is_valid():
            serializer.save()
            res = { "msg": "Data Created" }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')