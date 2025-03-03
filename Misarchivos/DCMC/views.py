from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def IndexView(request):

    return render(request, 'index.html')
# Compare this snippet from Misarchivos/DCMC/models.py:
# Compare this snippet from Misarchivos/DCMC/urls.py: