from django.shortcuts import render

# Create your views here.

def therapistview(request):
	question="Hello"
	data={
		'quest':question,
	}
	return render(request,"therapist.html",data)