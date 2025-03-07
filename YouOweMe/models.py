from django.db import models

class Debt(models.Model):
    name = models.CharField(max_length=100)
    purchase = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateField(auto_now=False)

    def __str__(self):
        return f"Debt of {str(self.total_amount)} generated on {self.effective_date} by {self.name}, on the purchase of a {self.purchase}."
    
class DeadBeat(models.Model):
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE, related_name='debt')
    name =  models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField(auto_now=False)

    def __str__(self):
        return f"{str(self.amount)} Paid by: {self.name} on {self.date}"
