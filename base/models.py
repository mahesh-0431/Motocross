from django.db import models
from django.contrib.auth.models import User



class Candidate(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class OfferLetter(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    agreement_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    interviewer = models.CharField(max_length=100)
    referrer = models.CharField(max_length=100)

    def __str__(self):
        return f"Offer Letter for {self.candidate.name}"