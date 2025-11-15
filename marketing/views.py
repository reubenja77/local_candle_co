from django.http import HttpResponse
# or: from django.shortcuts import render

def marketing_home(request):
    return HttpResponse("Marketing page coming soon for Local Candle Co.")
    # return render(request, "marketing/marketing_home.html")