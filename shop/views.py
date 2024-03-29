from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course, Category


def index(request):
    course_name = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': course_name})

def single_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course})

