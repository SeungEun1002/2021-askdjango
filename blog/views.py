from django.shortcuts import render
from django.http import HttpResponse

def index(request):
## return HttpResponse('Hello World')
    code = {
        'name': 'seungeun',
        'age': 29,
        'mydict' : {
            'subject': 'math',
            'time': 4,
        }
    }

    mentor_list=[
        {'name': 'name1', 'subject': 'math'},
        {'name': 'name2', 'subject': 'math'},
        {'name': 'name3', 'subject': 'english'},
        {'name': 'name4', 'subject': 'english'},
    ]
    context={
        'mentor_list': mentor_list
    }
    ## {'key': 'value'} #dictionary
    ## obj #class object

    return render(request, 'index.html', context) ##넘겨주는 변수 하나로 정리해서 넘겨주기
