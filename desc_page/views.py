from django.shortcuts import render

# Create your views here.

def description_page(request):
	return render(request, 'desc_page/description_page.html')