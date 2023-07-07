from django.shortcuts import render

post=[
    {
        'Authur':'Nelson Tommogo',
        'Title':'Geniuses Are not made',
        'Content':'The Content',
        'date_Posted':'August 21, 2022',
        
    },
     {
        'Authur':'Common Genius',
        'Title':'Python Programming',
        'Content':'The Content',
        'date_Posted':'January 11, 2021',
        
    },
    {
        'Authur':'Josephat Nanok',
        'Title':'Database Programming',
        'Content':'The Content',
        'date_Posted':'March 31, 2001',
        
    }
]

# Create your views here.
def home(request):
    return render(request, 'blogg/home.html')

def about(request):
    return render(request, 'blogg/about.html')
