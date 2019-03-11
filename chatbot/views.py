from django.shortcuts import render

# Create your views here.

def chatbotview(request):
	question="Hello"
	data={
		'quest':question,
	}
	return render(request,"bot.html",data)