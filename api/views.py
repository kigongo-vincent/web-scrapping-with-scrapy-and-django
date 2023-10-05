from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CancerSerializer
# from django.views.decorators.csrf import csrf_exempt
from .models import Cancer
import subprocess
# Create your views here.
@api_view(['GET','POST'])
def home(request):
    cancerdata = Cancer.objects.all()
    serialized = CancerSerializer(cancerdata, many = True)
    if request.method == 'POST':
        serialized = CancerSerializer(data = request.data)
        if serialized.is_valid():
            serialized.save()
            serialized = CancerSerializer(cancerdata, many = True)
    return Response(serialized.data)

def index(request):
    if request.method == 'POST':
        subprocess.run(['scrapy', 'crawl', 'cancerdat', '-a', 'port=8888'], check = True)
        return redirect('index')
    return render(request, 'index.html')

