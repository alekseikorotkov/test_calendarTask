"""Models module"""
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Country(models.Model):
    """Country model"""
    iso_code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.iso_code)

class Company(models.Model):
    """Company model"""
    title = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}'.format(self.title)

class Period(models.Model):
    """Period model"""
    CHOISE_STATUS = (
        ('new', 'New'),
        ('active', 'Active'),
        ('reconciliation', 'Reconciliation'),
        ('closed', 'Closed')
    )
    start = models.DateField()
    stop = models.DateField()
    status = models.CharField(max_length=50, choices=CHOISE_STATUS)

    def clean(self):
        if self.start > self.stop:
            raise ValidationError(
                ('date start is greater than end date'))

    def __str__(self):
        return 'From:{} To:{} Status:{}'.format(self.start, self.stop, self.status)


class Agreement(models.Model):
    """Agreement model"""
    negotiator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    start = models.DateField()
    stop = models.DateField()
    period = models.ManyToManyField(Period)

    def __str__(self):
        return '{} {} {} {}'.format(self.company.title, self.negotiator, self.start, self.stop)
