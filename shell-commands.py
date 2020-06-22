# Prepare Python:

sudo apt-get install python3 	#not necesary many distros have it preinstalled
sudo apt-get install python3-pip

# Prepare Virtual Environment:

pip3 install virtualenv
mkdir Dev	#can use any name for these folders
cd Dev
mkdir trydjango
cd trydjango

# Create Virtual Environment:

virtualenv -p python3 .
source bin/activate

Install Django:

pip install django==2.1.5

# VirtEnv Commands:

deactivate 	#To deactivate virtual env
source /bin/activate 	#To activate current folders virtual env


# Create blank django project

mkdir src
cd src

django-admin createproject trydjango .

# Start Django Server

python manage.py runserver
python manage.py makemigrations #??
python manage.py migrate    # Apply migrations/changes if you make any.

# Create Django SuperAdmin User

python manage.py createsuperuser  # i used Default user: pyweb


#Create Django App with name products

python manage.py startapp products

#Create Model

-Goto products folder created, and open models.py and add this code:

class Product(models.Model):
    title       = models.CharField(max_length=120) #max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField()

# Add Model to apps

-Goto Trydjango settings.py add to INSTALLED_APPS = [:

'products',

python manage.py makemigrations
python manage.py migrate

#Add this model to Admin:

-Goto Products folder admin.py and add:

from .models import Product
admin.site.register(Product)

-You can go to admin webpage now and check out and fill the fields and save data to database.

#To do this through python shell:

python manage.py shell

from products.models import Product

Product.objects.all() # shows saved entries.

Product.objects.create(title='ShellTest1', description='FromShellToApp', price='22.99', summary='sweet')


# Start a new app called 'Pages'

python manage.py startapp pages

-Goto pages folder views.py and add / edit :

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contacts View</h1>")

def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About View</h1>")

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social View</h1>")

    
#Add view to urls

-Goto trydjango urls.py and add:

from pages.views import home_view, contact_view, about_view, social_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('about/', about_view),
    path('contact/', contact_view),
    path('social/', social_view),
]

 




