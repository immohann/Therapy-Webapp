from django.shortcuts import render

# Create your views here.

def helplineview(request):
	question="Hello"
	data={
		'quest':question,
	}
	return render(request,"helpline.html",data)