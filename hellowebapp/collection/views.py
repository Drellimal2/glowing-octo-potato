from django.shortcuts import render

# Create your views here.

def index(request):
	number = 7
	return render(request, 'index.html', {'number': number})
