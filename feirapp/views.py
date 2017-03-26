from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from feirapp.models import Feira
from feirapp.serializers import FeiraSerializer
# Create your views here.

@csrf_exempt
def feira_list(request):
    """
    List all code feira, or create a new feira.
    """
    if request.method == 'GET':
        snippets = Feira.objects.all()
        serializer = FeiraSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeiraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
