from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Berry:
    def __init__(self, name, variety, description, season):
        self.name = name
        self.variety = variety
        self.description = description
        self.season = season
    
berries = [
    Berry('Strawberry', 'Hoods', 'smaller and more orange-y in color', 'summer'),
    Berry('Strawberry', 'Mary\'s Peak ', 'giant, square-shaped strawberries that tolerate harsher weather conditions', 'summer'),
    Berry('Strawberry', 'Sweet Sunrise', 'heart-shaped, red, and juicy strawberries that aren’t as sweet as Hoods', 'summer'),
    Berry('Strawberry', 'OSU Test Variety', 'large, juicy, sweet, and delicious', 'summer'),
]

def berry_index(request):
    return render(request, 'berries/index.html', {'berries': berries})