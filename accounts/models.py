from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UsersDetails(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=500)
    dob = models.DateField()
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.IntegerField()
    mob = models.IntegerField()

    def __str__(self, data):
        self.firstname = data.get('firstname')
        self.lastname = data.get('lastanme')
        self.email = data.get('email')
        self.username = self.email
        self.dob = data.get('dob')
        self.address = data.get('address')
        self.city = data.get('city')
        self.state = data.get('state')
        self.postcode = data.get('postcode')
        self.mob = data.get('mob')
        self.save()
        return self.firstname



    # def setUserData(self, data):
    #     self.firstname = data.get('firstname')
    #     self.lastname = data.get('lastanme')
    #     self.email = data.get('email')
    #     self.password = data.get('password')
    #     self.dob = data.get('dob')
    #     self.address = data.get('address')
    #     self.city = data.get('city')
    #     self.state = data.get('state')
    #     self.postcode = data.get('postcode')
    #     self.mob = data.get('mob')


def CreateUserModel(userdata):
    username = userdata.get('email')
    email = userdata.get('email')
    password = userdata.get('password')
    firstname = userdata.get('firstname')
    lastname = userdata.get('lastname')
    address = userdata.get('address')
    dob = userdata.get('dob')
    city = userdata.get('city')
    state = userdata.get('state')
    postcode = userdata.get('postcode')
    mob = userdata.get('mob')
    try:
        User.objects.get(username=username)
        return 'user already exist'
    except:
        user = User.objects.create_user(username=username, email=email, password=password,is_active=True)
        user.first_name = firstname
        user.last_name = lastname
        user.address = address
        user.dob = dob
        user.city = city
        user.state = state
        user.postcode = postcode
        user.mob = mob
        user.save()
        return 'user created'




