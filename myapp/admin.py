from django.contrib import admin
from .models import Role, Appraiser, Client, LoanStatus, Loan, Collateral, Payment

# Register Role model
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'permissions')  # Columns to display in admin list view
    search_fields = ('role_name',)  # Add search capability

# Register Appraiser model
@admin.register(Appraiser)
class AppraiserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'role')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('role',)  # Filter by role

# Register Client model
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'registration_date')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('registration_date',)  # Filter by registration date

# Register LoanStatus model
@admin.register(LoanStatus)
class LoanStatusAdmin(admin.ModelAdmin):
    list_display = ('status_name',)
    search_fields = ('status_name',)

# Register Loan model
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('client', 'loan_amount', 'interest_rate', 'loan_date', 'due_date', 'status')
    search_fields = ('client__first_name', 'client__last_name')  # Enable searching by client name
    list_filter = ('loan_date', 'due_date', 'status')

# Register Collateral model
@admin.register(Collateral)
class CollateralAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'client', 'appraised_value', 'appraiser', 'date_received', 'loan')
    search_fields = ('item_name', 'client__first_name', 'client__last_name')
    list_filter = ('date_received', 'appraiser')

# Register Payment model
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('loan', 'payment_date', 'payment_amount', 'remaining_balance', 'appraiser')
    search_fields = ('loan__client__first_name', 'loan__client__last_name')  # Enable searching by loan's client
    list_filter = ('payment_date',)
