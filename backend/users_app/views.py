from django.shortcuts import render
from users_app.models import User

# Create your views here.

def index_page(request):

    all_users = User.objects.all() #Model.manager.method_of_manager
    print(all_users)

    return render (request, 'index.html')