# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date


 # Find students with last name "Smith"
learners_smith = Learner.objects.filter(#<HINT> add last_name check)
print("1. Find learners with last name `Smith`")
try:
    learner_smith = Learner.objects.get(last_name="Smith")
except Learner.DoesNotExist:
    print("Learner Smith doesn't exist")
print("\n")

# Order by dob descending, and select the first two objects
print("2. Find top two youngest learners")
try:
    youngest_learners = Learner.objects.order_by('-dob')[0:2]
except:
    print(
        "No learners found"
    )
print(youngest_learners)