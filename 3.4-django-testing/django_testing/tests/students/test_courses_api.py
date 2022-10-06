from audioop import reverse
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_course(client):
    """
    тест успешного получения курса "GET" запросом
    """
    Course.objects.create(name='python')
    response = client.get('/api/v1/courses/')
    
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == 'python'
    
@pytest.mark.django_db
def test_course_create(client):
    """
    тест успешного создания курса 'POST' запросом
    с передачей json файла с курсом
    """
    count = Course.objects.count()
    response = client.post(
        '/api/v1/courses/', 
        data={'name': 'java'}
        )
    
    assert response.status_code == 201
    assert Course.objects.count() == count+1
    
@pytest.mark.django_db
def test_course_delete(client):
    """
    тест успешного удаления курса
    """
    Course.objects.create(id=1, name='python')      # Создаем курс "python"
    response = client.delete('/api/v1/courses/1/')
    
    assert response.status_code == 204
    
@pytest.mark.django_db
def test_course_patch(client):
    """
    тест успешного обновления курса
    """
    course=Course.objects.create(name='python')    # Создаем курс "python"
    response = client.patch(f'/api/v1/courses/{course.id}/', data={'name': 'java'})  # Меняем на "java" patch запросом
    assert response.status_code == 200
    resp = client.get('/api/v1/courses/') # Делаем запрос курсов
    data = resp.json()
    assert data[0]['name'] == 'java'  # Проверяем возвращается ли нам именно 'java', a не изнаальный 'python'

@pytest.mark.django_db
def test_courses_get(client, courses_factory):
    """
    Тест успешного создания нескольких курсов с помощью bakery и 
    их получения 'GET' запросом
    """
    courses = courses_factory(_quantity = 10)
    url = reverse('courses-list')
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_id(client, courses_factory):
    """
    проверка фильтрации списка курсов по id
    создаем курсы через фабрику, передать id одного курса в фильтр, проверить результат запроса с фильтром
    """
    course = courses_factory(_quantity=10)
    url = '/api/v1/courses/'
    response = client.get(url, data={'id':f'{course[0].id}'})
    assert response.status_code == 200  
    data = response.json()
    assert data[0]['id'] == course[0].id



@pytest.mark.django_db
def test_filter_name(client):
    """
    проверка фильтрации списка курсов по 'name' при создании вручную
    """
    Course.objects.create(name='python')
    Course.objects.create(name='java')
    Course.objects.create(name='Ruby')
    url = '/api/v1/courses/?name=java'
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == 'java'
    
    
@pytest.mark.django_db
def test_filter_name_bakery(client, courses_factory):
    """
    проверка фильтрации списка курсов по 'name' при генерации
    с помощью bakery
    """
    course = courses_factory(_quantity=10)
    url = '/api/v1/courses/'
    response = client.get(url, data={'name':f'{course[1].name}'})
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course[1].name