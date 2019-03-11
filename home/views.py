from django.shortcuts import render

# Create your views here.

def homeview(request):
	question="Hello"
	data={
		'quest':question,
	}
	return render(request,"index.html",data)