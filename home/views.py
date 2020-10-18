from django.shortcuts import render

from home.forms import postform

# Create your views here.


def test(request):


	context = {	
		
	}
	return render(request, 'test.html', context)



def nav(request):


	context = {
		
	}
	return render(request, 'nav.html', context)


def home(request):
	form = postform(request.POST or None)
	if form.is_valid():
		form.save()
		form = postform

	else:
		bad = form.errors
		

	context = {'form':form, 'bad':bad}

	return render(request, 'index.html' , context)


