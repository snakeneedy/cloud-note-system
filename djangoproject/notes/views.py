from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def hello_world (request):
    htmlcode = """<!DOCTYPE html>
<html>
<head>
</head>
<body>
    <p>Hello World! {current_time}</p>
</body>
</html>
    """.format(current_time=datetime.now())
    return HttpResponse(htmlcode)

