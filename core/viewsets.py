from rest_framework.views import APIView
from rest_framework.response import Response

from utils import client


class Test1ViewSet(APIView):
    def get(self, request):
        db = client["default_db"]
        collection = db["hotel1"]
        result = collection.find({})[0]
        result.pop('_id')
        return Response({"result": result})


class Test2ViewSet(APIView):
    def get(self, request):
        db = client["default_db"]
        collection = db["hotel2"]
        result = collection.find({})[0]
        result.pop('_id')
        return Response({"result": result})
