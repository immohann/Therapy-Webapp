from django.shortcuts import render
from .form import LoginForm,SignupForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.


def loginregisterview(request):
	if 'login' in request.POST:
		loginview(request)
	elif 'signup' in request.POST:
		signupview(request)
	form = LoginForm()
	forms = SignupForm()
	return render(request,"login.html",{'form':form,'forms':forms})


def loginview(request):
	if request.method == 'POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			print(email,password)
			user = authenticate(username = email, password = password)
			if user is not None:
				print("Successful")
				login(request,user)
				return redirect('/therapy/home/')
			else:
				message = "Invalid Email id or Password. Please Try Again!!"
				return render(request,"login.html",{'form':form,'message':message})

	else:
		form = LoginForm()
	return render(request,"login.html",{'form':form})


def signupview(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = True
			to_email = form.cleaned_data.get('email')
			user.username = to_email
			user_list=User.objects.all()
			for query in user_list:
				if user.username in query.username:
					error = "Email Already Exists . "
					return render(request, 'login.html', {'forms': form,'error':error})
			user.save()
			return render(request, 'login.html', {'forms': form})
			# current_site = get_current_site(request)
			# message = render_to_string('account_activation_email.html', {
			# 	'user':user, 
			# 	'domain':current_site.domain,
			# 	'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
			# 	'token': account_activation_token.make_token(user),
			# })
			# mail_subject = 'Activate your account.'
			# email = EmailMessage(mail_subject, message, to=[to_email])
			# email.send()
			# messages = 'Please confirm your email address to complete the registration'
			# return render(request, 'login.html', {'forms': form,'message':messages})
			# return HttpResponse('Please confirm your email address to complete the registration')
	else:
		form = SignupForm()
	return render(request, 'login.html', {'forms': form})

# def account_activation_sent(request):
#     return render(request, "account_activation_sent.html")


# def activate(request, uidb64, token):
# 	try:
# 		uid = force_text(urlsafe_base64_decode(uidb64))
# 		print(uid)
# 		user = User.objects.get(pk=uid)
# 	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
# 		user = None
# 	if user is not None and account_activation_token.check_token(user, token):
# 		user.is_active = True
# 		user.profile.email_confirmed = True
# 		user.save()
# 		login(request, user)
# 		return redirect('/therapy/home/')
# 	else:
# 		return HttpResponse('Activation link is invalid!')