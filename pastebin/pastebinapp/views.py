import os
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from utils import generate_crc32
from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def create_pastebin(request):
    if request.method == "POST":
        data = json.loads(request.body)
        input_text = data.get("inputText", "")
        hash = generate_crc32(input_text)
    return HttpResponse(f'"url":"http://{os.environ.get("SERVER_IP")}/{hash}"')
