from django.db import models


class Header(models.Model):
    me_header = models.ImageField(upload_to='backend/portbackend/assets/header')
    role = models.CharField(max_length=100)
    social1 = models.CharField(max_length=50) 
    social2 = models.CharField(max_length=50) 
    social3 = models.CharField(max_length=50)
    social4 = models.CharField(max_length=50)

    # STANDARDS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.role

class CardAbout(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    
    # STANDARDS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.description


class About(models.Model):
    me_about = models.ImageField(upload_to='backend/portbackend/assets/about')
    card_about = models.ForeignKey(CardAbout, on_delete=models.CASCADE)
    my_bio = models.CharField(max_length=300)
    
    # STANDARDS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.my_bio

class Competence(models.Model):
    title = models.CharField(max_length=50)
    icone = models.CharField(max_length=20)
    competence = models.CharField(max_length=50)
    rating = models.CharField(max_length=30)

    # STANDARDS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class LearnMore(models.Model):
    content = models.TextField()

    # STANDARDS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.content

class Service(models.Model):
    title = models.CharField(max_length=255)
    title_details = models.TextField()
    photo_serv = models.ImageField(upload_to='backend/portbackend/assets/service')
    learn_more = models.ForeignKey(LearnMore, null=True, blank=True, on_delete=models.CASCADE)

    # STANDARDS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.ImageField()
    review = models.TextField()

    # STANDARDS
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.review


# newsletter
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



