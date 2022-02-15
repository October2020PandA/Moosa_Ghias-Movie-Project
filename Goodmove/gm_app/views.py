from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import tmdbsimple as tmdb
import requests
import decouple


# from decouple import config.
api_key = decouple.config('api_key')
base_url = 'https://api.themoviedb.org/3/'

# Create your views here.
# movielist = ["movie1","movie2","movie3", "movie4", "movie5", "movie6", "movie7", "movie8", "movie9", "movie10"]

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.reg_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name= request.POST['last_name'], email = request.POST['email'], password = hashed_pw)
        request.session['user_id'] = new_user.id
        return redirect('/enter')
    return redirect('/')

    if request.method == 'POST':
        errors = User.objects.reg_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name= request.POST['last_name'], email = request.POST['email'], passoword = hashed_pw )
        request.session['user_id'] = new_user.id
        return redirect('/enter')
    return redirect('/')



def login(request):
    if request.method == 'POST':
        errors = User.objects.log_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = this_user.id
        return redirect('/enter')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def enter(request):
    if 'user_id' not in request.session:
        return redirect('/')
    url = f'{base_url}movie/popular?api_key={api_key}&language=en-US&page=1'
    popular = requests.get(url)
    result = popular.json()
    movies = {'popular': result}
    return render(request, 'enter.html', movies)

def search(request):
    if 'user_id' not in request.session:
        return redirect('/')
    query = request.POST['search']
    url = f'{base_url}search/movie?api_key={api_key}&query={query}&page=1&include_adult=True'
    the_search = requests.get(url)
    result = the_search.json()
    print(result) 
    movies = {'results': result}
    return render(request, 'search.html', movies)


def details(request,movie_id):
    # url = f'{base_url}movie/{movie_id}?api_key={api_key}&language=en-US&page=1'
    # response = requests.get(url)
    # movies = {'moviedetail':response.json()}
    # return render(request, 'movie_details.html', context=movies)
    
    if 'user_id' not in request.session:
        return redirect('/')
    url = f'{base_url}movie/{movie_id}?api_key={api_key}&language=en-US'
    the_movie = requests.get(url)
    detail = the_movie.json()
    context = {'details':detail}
    return render(request,'details.html',context)

def add(request,movie_id):
    if 'user_id' not in request.session:
        return redirect('/')
    url = f'{base_url}movie/{movie_id}?api_key={api_key}&language=en-US'
    the_movie = requests.get(url)
    detail = the_movie.json()
    context = {'details':detail}
    Film.objects.create(name=detail.get("original_title"),length= detail.get("runtime"), user = User.objects.get(id= request.session['user_id']))
    return redirect('/choices')
    

def choices(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id = request.session['user_id'])
    context = {
        'films':Film.objects.all(),
        'user':user

    }
    return render(request, 'choices.html', context)

def delete(request, movie_id):
    if 'user_id' not in request.session:
        return redirect('/')
    to_delete = Film.objects.get(id = movie_id)
    to_delete.delete()
    return redirect('/choices')

# https://api.themoviedb.org/3/movie/299536/?api_key=f1674b5242caff66ee3c4bfcbe5726cc&language=en-US
# https://api.themoviedb.org/3/movie/299536?api_key=f1674b5242caff66ee3c4bfcbe5726cc&language=en-US
