import json
import os
import subprocess
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files import File



# Create your views here.


def check_view(request):
    form_data = request.POST

    # user 이름과 answer 코드 user_output으로 받기 
    user_output = {}
    for key, value in form_data.items():
        user_output[key] = value
    
    # input 케이스 추가하기
    file_path = os.getcwd() + "\\codeserver\\testcase\\input.txt"
    test_inputs = []
    with open(file_path, 'r') as f:
        line = f.readline()
        # print(f.readlines())
        while line:
            if line != '\n':
                test_inputs.append(line.strip('\n'))
            line = f.readline()

    # output 케이스 추가하기
    file_path = os.getcwd() + "\\codeserver\\testcase\\output.txt"
    outputs = []
    with open(file_path, 'r') as f:
        tmp = []
        line = f.readline()

        while line:
            if line != '\n':
                tmp = line.strip('\n').split()
            elif line == '\n':
                outputs.append(tmp)
            line = f.readline()

    # answer 코드를 answer.txt에 추가하기
    code_file_path = os.getcwd() + "\\codeserver\\testcase\\answer.py"
    with open(code_file_path, 'w') as f:
        line = f.writelines(user_output['answer'])
        while line:
            line = f.writelines(user_output['answer'])
    
    # 테스트 케이스 값 넣기

    for i, input in enumerate(test_inputs):
        command = f'echo {input} | python {code_file_path}'
        result = subprocess.run(command, text=True, shell=True, stdout=subprocess.PIPE).stdout
        result = list(result)

        cnt = 0
        output = outputs[i]
        for out in output:
            # print('out: ', out, 'result', result[cnt])
            if result[cnt] == '\n':
                cnt += 1

            if result[cnt] != out:
                return HttpResponse('failed')
            cnt += 1
                        

    return HttpResponse('success')
    
