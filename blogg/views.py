from django.shortcuts import render

post=[
    {
        'author':'Nelson Tommogo',
        'title':'Geniuses Are not made',
        'content':'The Content',
        'date_Posted':'August 21, 2022',
        
    },
    {
        'author':'Josephat Nanok',
        'title':'Database Programming',
        'content':'The Content',
        'date_Posted':'March 31, 2001',
        
    }
]

# Create your views here.
def home(request):
    context={
        'posts':post
    }
    return render(request, 'blogg/home.html',context)

def about(request):
    return render(request, 'blogg/about.html')
