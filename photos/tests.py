from django.test import TestCase
from .models import Category, Neighbourhood,Business
from django.contrib.auth.models import User

# Create your tests here.

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.user=User(username='lola')
        self.user.save()
        self.profile=Neighbourhood(user=self.user,name='kakashi',bio='ninja should fight.',profile_pic='default.png')
    def tearDown(self):
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_saveNeighbourhood(self):
        self.profile.save_profile()
        neighbourhood_saved = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood_saved) > 0)
        
class BusinessTestClass(TestCase):
    def setUp(self):
        self.category=Category(username='laundry')
        self.category.save()
        self.category=Business(user=self.user,name='john',description='feel free to buy our clothes',image='default.png')
    def tearDown(self):
          Category.objects.all().delete()
          Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_saveBusiness(self):
        self.category.save_business()
        business_saved = Business.objects.all()
        self.assertTrue(len(business_saved) > 0)