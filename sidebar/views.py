import requests
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Anouncement
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
def latest_posts(request):
    context = {
        'posts' : Post.objects.all().order_by('-date_posted')[:5],
        'title' : 'Latest Posts'
    }
    return render(request, 'sidebar/latest_posts.html', context)
    
def anouncements(request):
    context = {
        'anouncements' : Anouncement.objects.all().order_by('-date_posted'),
        'title' : 'Anouncements'
    }
    return render(request, 'sidebar/anouncements.html', context)

class AnouncementListView(ListView):
    model = Anouncement
    template_name = 'sidebar/anouncements.html' # <app> / <model>_<viewtype>.html
    context_object_name = 'anouncements'
    ordering = ['-date_posted'] # for ordering the newest blog to the top of the page.
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Announcements'
        return context

class UserAnouncementListView(ListView):
    model = Anouncement
    template_name = 'sidebar/user_anouncements.html' # <app> / <model>_<viewtype>.html
    context_object_name = 'anouncements'
    paginate_by = 4
    
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Anouncement.objects.filter(author = user).order_by('-date_posted')
    """ 
     the upper function 'get_queryset' must be this spelling. if there occurs any mispelling 
     then the posts of every particular author will not be shown correctly at
     user_posts.html page.
    """
    
class AnouncementDetailView(DetailView):
    model = Anouncement
    
class AnouncementCreateView( LoginRequiredMixin, CreateView):
    model = Anouncement
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AnouncementUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Anouncement
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class AnouncementDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Anouncement
    success_url = reverse_lazy('sidebar_anouncement_list')
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def weather(request):
    # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
    api_key = '30d4741c779ba94c470ca1f63045390a'
    city = request.GET.get('city')
    country = request.GET.get('country')

    if city and country:
        area = f'{city}, {country}'
    else:
        area = 'dhaka, bangladesh'
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={area}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    # wind and wind direction part starts.
    if 'wind' in data:
        direction = data['wind']['deg']
    else:
        direction = 404
        
    if direction > 337.5 or direction <= 22.5:
        direction = 'N'
    elif direction > 22.5 and direction <= 67.5:
        direction = 'NE'
    elif direction > 67.5 and direction <= 112.5:
        direction = 'E'
    elif direction > 112.5 and direction <= 157.5:
        direction = 'SE'
    elif direction > 157.5 and direction <= 202.5:
        direction = 'S'
    elif direction > 202.5 and direction <= 247.5:
        direction = 'SW'
    elif direction > 247.5 and direction <= 292.5:
        direction = 'W'
    elif direction > 292.5 and direction <= 337.5:
        direction = 'NW'
    elif direction == 404:
        direction = 'N/A'
    else:
        pass
    # wind and wind direction part ends.
    
    # sunrise, sunset and timezone part starts.
    from datetime import datetime
    if data['cod'] != '404':
        timezone = int(data['timezone'])
        
        sunrise_utc = int(data['sys']['sunrise'])
        sunrise_local = datetime.utcfromtimestamp(sunrise_utc + timezone).strftime('%I:%M %p')

        sunset_utc = int(data['sys']['sunset'])
        sunset_local = datetime.utcfromtimestamp(sunset_utc + timezone).strftime('%I:%M %p')
    # sunrise, sunset and timezone part ends.
    else:
        timezone = 0
        sunrise_local = 'N/A'
        sunset_local = 'N/A'
    
    # weather info part starts.
    if response.status_code == 200:
        weather_info = {
            'Temperature': f"{data['main']['temp']}°C",
            'Feels like': f"{data['main']['feels_like']}°C",
            'Air pressure': f"{data['main']['pressure']} hPa", 
            'Description': f"{data['weather'][0]['description']}", 
            'humidity': f"{data['main']['humidity']}%",
            'Visibility': f"{data['visibility'] / 1000} km",
            'Wind speed': f"{data['wind']['speed']} km/h", 
            'Wind deg': f"{data['wind']['deg']}° {direction}",
            'Wind dir': direction,
            'Lat' : f"{data['coord']['lat']}°",
            'Lon' : f"{data['coord']['lon']}°",
            'Sunrise' : sunrise_local, 
            'Sunset' : sunset_local,
            'Timezone' : timezone,
            'City' : f"{data['name']}",
            'Country' : f"{data['sys']['country']}",
        }  
    else:
        weather_info = None
    # weather info part ends.
    
    context = {
        'data' : weather_info,
        'title' : 'Weather',
    }
    
    return render(request, 'sidebar/weather.html', context)
    

        





    

    






