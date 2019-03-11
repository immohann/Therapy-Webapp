from django.shortcuts import render

# Create your views here.

def dietitianview(request):
	question="Hello"
	data={
		'quest':question,
	}
	return render(request,"dietitian.html",data)