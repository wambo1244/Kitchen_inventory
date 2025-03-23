from django.shortcuts import render, redirect
from .models import Ingredient, Inventory, Order, Supplier
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
                                    

def ingredients_view(request):
    ingredients = Ingredient.objects.all()
    suppliers = Supplier.objects.all()
    return render(request, 'your_template.html', {'ingredients': ingredients, 'suppliers': suppliers})

def inventory_list(request):
    inventory = Inventory.objects.all()
    ingredients = Ingredient.objects.all()  # This retrieves all ingredients
    suppliers = Supplier.objects.all()  # This retrieves all suppliers
    
    return render(request, 'inventory/inventory_list.html', {
        'inventory': inventory,
        'ingredients': ingredients,
        'suppliers': suppliers
    })

def create_order(request):
    if request.method == 'POST':
        ingredient_id = request.POST.get('ingredient_id')
        quantity = request.POST.get('quantity')
        ingredient = Ingredient.objects.get(id=ingredient_id)
        order = Order(ingredient=ingredient, quantity_ordered=quantity)
        order.save()
        return HttpResponse('Order placed successfully!')
    else:
        ingredients = Ingredient.objects.all()
        return render(request, 'inventory/create_order.html', {'ingredients': ingredients})
# Define user permission checks
def usage_report(request):
    # Get date range from request or use current time
    start_date = request.GET.get('start_date', timezone.now())
    end_date = request.GET.get('end_date', timezone.now())

    # Query for orders within the date range
    orders = Order.objects.filter(date_ordered__range=[start_date, end_date])

    # Return the response with the report
    return render(request, 'inventory/usage_report.html', {'orders': orders})

def is_storekeeper(user):
    return user.groups.filter(name='Storekeeper').exists()

def is_catering_officer(user):
    return user.groups.filter(name='Catering Officer').exists()

def is_assistant_catering_officer(user):
    return user.groups.filter(name='Assistant Catering Officer').exists()


# Dashboard views for each user group
@login_required
@user_passes_test(is_storekeeper)
def storekeeper_dashboard(request):
    return render(request, 'accounts/storekeeper_dashboard.html')

@login_required
@user_passes_test(is_catering_officer)
def catering_officer_dashboard(request):
    return render(request, 'accounts/catering_officer_dashboard.html')

@login_required
@user_passes_test(is_assistant_catering_officer)
def assistant_catering_officer_dashboard(request):
    return render(request, 'accounts/assistant_catering_officer_dashboard.html')

@login_required
def default_dashboard(request):
    return render(request, 'accounts/default_dashboard.html')

# Login view to authenticate users
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Debugging: Print the user's groups
            print(f'User {user.username} belongs to groups: {user.groups.all()}')

            # Redirect based on group
            if user.groups.filter(name='Storekeeper').exists():
                return redirect('storekeeper_dashboard')
            elif user.groups.filter(name='Catering Officer').exists():
                return redirect('catering_officer_dashboard')
            elif user.groups.filter(name='Assistant Catering Officer').exists():
                return redirect('assistant_catering_officer_dashboard')
            else:
                return redirect('default_dashboard')  # Default if no group assigned

        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    return render(request, 'accounts/login.html')


# Home page view
def home(request):
    inventory = Inventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {'inventory': inventory})

