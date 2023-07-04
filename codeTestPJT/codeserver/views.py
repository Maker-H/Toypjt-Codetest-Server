import json
import os
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files import File



# Create your views here.


def check_view(request):
    form_data = request.POST

    user_output = {}
    for key, value in form_data.items():
        user_output[key] = value
    
    file_path = os.getcwd() + "\\input.txt"
    inputs = []
    with open(file_path, 'r') as f:
        line = f.readline()
        # print(f.readlines())
        while line:
            if line != '\n':
                inputs.append(line.strip('\n'))
            line = f.readline()

    file_path = os.getcwd() + "\\output.txt"
    outputs = []
    with open(file_path, 'r') as f:
        line = f.readline()
        # print(f.readlines())
        while line:
            if line != '\n':
                outputs.append(line.strip('\n'))
            line = f.readline()


    return HttpResponse(json.dumps(outputs), content_type='application/json')
    
