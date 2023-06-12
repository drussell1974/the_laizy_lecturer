from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def assess_student_work(request):
    
    if request.method == 'POST':
        # Extract the data from the request
        rubric = request.POST.get('rubric')
        student_work = request.POST.get('student_work')
        rubric_scores = request.POST.get('rubric_scores')

        # Make a request to the API
        api_url = 'http://127.0.0.1/assess-student-work'  # Replace with your actual API URL
        response = requests.post(api_url, json={
            'rubric': rubric,
            'student_work': student_work,
            'rubric_scores': rubric_scores
        })

        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data)
        else:
            error_message = "Failed to assess student work. Please try again later."
            return JsonResponse({'error': error_message}, status=500)

    return render(request, 'uiapp/assess_student_work.html')
