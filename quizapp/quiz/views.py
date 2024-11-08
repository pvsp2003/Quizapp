from django.shortcuts import render,redirect
from .models import Question
from .models import Score
from .models import Log
import json

# Create your views here.
def homepage(request):
    obj=Log.objects.first()
    obj.login+=1
    obj.save()
    if obj.login==1:
        return render(request, 'whome.html')
    else:
        return render(request,'home.html',{'login':obj.login})
def quizpage(request, subject):
    obj=Score.objects.filter(sub=subject)
    if obj.exists():
        return render(request, 'completed.html', {'marks': obj[0].marks, 'subject': subject})
    else:
        questions = Question.objects.filter(sub=subject)
        que = []

        # Structure the questions as needed for the front-end
        for question in questions:
            que.append({
                'subject': question.sub,
                'question': question.question,
                'options': [
                    question.option1.strip(),
                    question.option2.strip(),
                    question.option3.strip(),
                    question.option4.strip()
                ],
                'correct': question.correctoption.strip()# Store the correct option's value
            })

        context = {
            'questions_json': json.dumps(que)  # Convert the list to JSON
        }
        return render(request, 'ques.html', context)
def updatescore(request, subject, marks):
    ob=Score.objects.create(
        sub=subject,
        marks=marks
    )
    ob.save()
    return render(request, 'completed.html', {'marks': marks, 'subject': subject})
def analytics(request):
    l=[]
    ob=Score.objects.all()
    math='null'
    sci='null'
    geo='null'
    comp='null'
    for sobj in ob:
        if sobj.sub=='math':
            math=sobj.marks
        elif sobj.sub=='science':
            sci=sobj.marks
        elif sobj.sub=='geography':
            geo=sobj.marks
        elif sobj.sub=='computer':
            comp=sobj.marks
    return render(request, 'graph.html',{'math':math,'sci':sci,'geo':geo,'comp':comp})
def deletedata(request):
    Score.objects.all().delete()
    return render(request, 'graph.html',{'math':'null','sci':'null','geo':'null','comp':'null'})
def whome(request):
    return render(request, 'whome.html')
def wques(request):
    questions = [
        {
            'question': 'What is 1 + 1?',
            'options': ['0', '1', '2', '3'],
            'correct': '2',
            'subject': 'Mathematics'
        },
        {
            'question': 'What is 1 - 1?',
            'options': ['1', '0', '3', '2'],
            'correct': '0',
            'subject': 'Mathematics'
        },
        
    ]
    questions_json = json.dumps(questions)  # Convert to JSON for the frontend
    return render(request, 'wques.html', {'questions_json': questions_json})
def wcompleted(request,marks):
    return render(request,'wcompleted.html',{'score':marks})
def whome2(request):
    return render(request, 'whome2.html')
def wgraph(request):
    return render(request, 'wgraph.html')
def exphome(request):
    obj=Log.objects.first()
    obj.login=1
    obj.save()
    return render(request, 'whome.html')