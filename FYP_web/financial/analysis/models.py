from django.db import models


class userLogin(models.Model):
    ID_text = models.CharField(max_length=10)
    PW_text = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')


class UserInfro(models.Model):
    UserLogin = models.ForeignKey(userLogin, on_delete=models.CASCADE)
    age = models.IntegerField(default=25)
    education = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    houseInfo = models.CharField(max_length=200)
    Maritalstatus = models.CharField(max_length=200)
    Occupation = models.CharField(max_length=200)

    monthySalary = models.CharField(max_length=200)
    OtherMonthlyIncome = models.CharField(max_length=200)
    SavingBalance = models.CharField(max_length=200)
    Investment = models.CharField(max_length=200)
    Property = models.CharField(max_length=200)
    CreditCardLiabilities = models.CharField(max_length=200)
    HomeMortgage = models.CharField(max_length=200)
    OtherLoan = models.CharField(max_length=200)
    Foodspend = models.CharField(max_length=200)
    clothingspend = models.CharField(max_length=200)
    shopping = models.CharField(max_length=200)
    accommodation = models.CharField(max_length=200)
    Transport = models.CharField(max_length=200)
    othersMonthlyspend = models.CharField(max_length=200)




