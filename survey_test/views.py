from django.shortcuts import render

# Create your views here.

marks = 0

def survey_testview(request):
    
	
#    if '1a' in request.POST:
#        marks=marks+0
#        print(marks)
#    if '1b' in request.POST:
#        marks=marks+5
#    if '1c' in request.POST:
#        marks=marks+10
#    if '1d' in request.POST:
#        marks=marks+15
#    if '2a' in request.POST:
#        marks=marks+0
#    if '2b' in request.POST:
#        marks=marks+5
#    if '2c' in request.POST:
#        marks=marks+10
#    if '2d' in request.POST:
#        marks=marks+15
#    if '3a' in request.POST:
#        marks=marks+0
#    if '3b' in request.POST:
#        marks=marks+5
#    if '3c' in request.POST:
#        marks=marks+10
#    if '3d' in request.POST:
#        marks=marks+15
#    if '4a' in request.POST:
#        marks=marks+0
#    if '4b' in request.POST:
#        marks=marks+5
#    if '4c' in request.POST:
#        marks=marks+10
#    if '4d' in request.POST:
#        marks=marks+15
#    if '5a' in request.POST:
#        marks=marks+0
#    if '5b' in request.POST:
#        marks=marks+5
#    if '5c' in request.POST:
#        marks=marks+10
#    if '5d' in request.POST:
#        marks=marks+15
#    else:
#        return render(request,"test.html")
#    if marks in range(0,18):
#        message="Happy"
#    elif marks in range(18,36):
#        message = "satisfied"
#    elif marks in range(36,51):
#        message = "mildy depressed"
#    else:
#        message = "very depressed"
#    data={'message':message,}
#    print(data)
#    if 'result' in request.POST:
#        return render(request,"test.html",data)
#    return render(request,"test.html",data)
#    if request.POST:
#        if 'result' in request.POST:
#            message = "VERY DEPRESSED"
#            data={'message':message}
#            return render(request,"test.html",data)
#        else:
#            return render(request,"test.html")
    message = "VERY DEPRESSED"
    data={'message':message}
    return render(request,"test.html",data)
#    else:
#        return render(request,"test.html")