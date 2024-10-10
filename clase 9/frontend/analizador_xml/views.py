from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests


def xml_view(request):
    xml_input = ""
    xml_output = ""

    if request.method == 'POST':
        if 'analyze' in request.POST:
            xml_input = request.POST.get('xml_input', '')
            response = requests.post('http://localhost:5000/analizar', data={'xml': xml_input})
            if response.status_code == 200:
                xml_output = response.json().get('message')
            return render(request, 'xml_form.html', {'xml_input': xml_input, 'xml_output': xml_output})
        elif 'result' in request.POST:
            response = requests.get('http://localhost:5000/resultado')
            if response.status_code == 200:
                xml_output = response.text
            return render(request, 'xml_form.html', {'xml_input': xml_input, 'xml_output': xml_output})
        elif 'reset' in request.POST:
            return render(request, 'xml_form.html', {'xml_input': "", 'xml_output': ""})

    return render(request, 'xml_form.html', {'xml_input': "", 'xml_output': ""})
