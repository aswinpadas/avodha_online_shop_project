from django.db import models


# Create your models here.
class UsersDB(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    username=models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    dob = models.DateField()
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.IntegerField()
    mob = models.IntegerField()

    def __str__(self,data):
        self.firstname = data.get('firstname')
        self.lastname = data.get('lastanme')
        self.email = data.get('email')
        self.username=self.email
        self.password = data.get('password')
        self.dob = data.get('dob')
        self.address = data.get('address')
        self.city = data.get('city')
        self.state = data.get('state')
        self.postcode = data.get('postcode')
        self.mob = data.get('mob')
        self.save()
        return self.firstname


    def validateUser(self,email,password):
        if self.email==email and self.password==password:
            return True
        else:
            return False

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
