from django.shortcuts import render

# Create your views here.

def storiesview(request):
	question="Hello"
	data={
		'quest':question,
	}
	return render(request,"stories.html",data)