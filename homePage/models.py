from django.db import models


class Products(models.Model):
    picture= models.ImageField(upload_to='images/',null= True)
    product_name= models.CharField(max_length=12, null=True)
    start_date= models.DateField(null=True)
    end_date= models.DateField(null=True)

class Register(models.Model):
    name= models.CharField(
        max_length=30, null= True
    )
    email= models.EmailField(
        null=True
    )
    gender_choice=(
        ('Female','Female'),
        ('male','male'),
        ('none','none')
    )
    gender= models.CharField(
        max_length=8, choices=gender_choice
    )

    national_id= models.CharField(
        max_length=20, null=True
    )

    description= models.TextField(
        max_length=299, null=True
    )

    attachment= models.FileField(
        upload_to='documents/', default='SOME STRING'
    )

