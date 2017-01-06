from django.shortcuts import render
from Users.models import Chat
# Create your views here.
def login(request):
	next=request.GET.get('next', '/home')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				return HttpResponse("Account is not active")
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, "Users/login.html",{'next':next})
def logout(request):
	logout(request)
	return HttpResponseRedirect('/login/')

def Home(request):
	c= Chat.objects.all()
	return render(request,'Users/home.html',{'home':'active', 'chat':c})

def Post(request):
	if request.method=="POST":
		msg = request.POST.get('msgbox',None)
		print('******************')
		print(msg)
		c = Chat(user=request.user,message=msg)
		if msg != '':
			c.save()
		return JsonResponse({'msg':msg, 'user':c.user.username})
	else:
		return HttpResponse('Request must be POST')

def Messages(request):
	c=Chat.objects.all()
	return render(request,'Users/messages.html',{'chat':c})