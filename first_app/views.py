from django.shortcuts import render

# Create your views here.


def contact(request):
    return render(request, './first_app/index.html', {'author': 'phitron', 'age': 19, 'marks': 90, 'courses': [
        {
            'id': 1,
            'course': 'C',
            'teacher': 'Arifin'
        },
        {
            'id': 2,
            'course': 'C++',
            'teacher': 'Rokey'
        },
        {
            'id': 3,
            'course': 'Database',
            'teacher': 'Iftekhar'
        },
    ], 'name': 'Tanver', 'lst': [1, 2, 4, 7], 'blog': 'I am Tanver Rana Sobur. I am the student of Bangladesh University department of CSE. THis is our blog website.'})
