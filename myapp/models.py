from django.db import models

# Roles model
class Role(models.Model):
    role_name = models.CharField(max_length=45, unique=True)
    permissions = models.TextField()

    def __str__(self):
        return self.role_name

# Appraisers model
class Appraiser(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Clients model
class Client(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    registration_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# LoanStatus model
class LoanStatus(models.Model):
    status_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.status_name

# Loans model
class Loan(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_date = models.DateField()
    due_date = models.DateField()
    status = models.ForeignKey(LoanStatus, on_delete=models.CASCADE)

    def __str__(self):
        return f'Loan {self.id} for {self.client}'

# Collateral model
class Collateral(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    appraised_value = models.DecimalField(max_digits=10, decimal_places=2)
    appraiser = models.ForeignKey(Appraiser, on_delete=models.CASCADE)
    date_received = models.DateField()
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item_name} (Client: {self.client})'

# Payments model
class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2)
    appraiser = models.ForeignKey(Appraiser, on_delete=models.CASCADE)

    def __str__(self):
        return f'Payment {self.id} for Loan {self.loan}'
