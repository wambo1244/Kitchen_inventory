from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingredient, Inventory, Order, Supplier
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SupplierForm

# Add Supplier
@login_required
def add_supplier(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        address = request.POST.get("address")

        # Create new supplier
        Supplier.objects.create(
            name=name,
            contact=contact,
            email=email,
            address=address
        )

        return redirect("catering_officer_dashboard")  # Redirect after successfully adding the supplier

    return render(request, 'accounts/add_supplier.html')  # Render the add supplier form if GET request
# Edit Supplier
@login_required
def edit_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == "POST":
        supplier.name = request.POST["name"]
        supplier.contact = request.POST["contact"]
        supplier.email = request.POST["email"]
        supplier.address = request.POST["address"]
        supplier.save()

    return redirect("catering_officer_dashboard")

# Delete Supplier
@login_required
def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    supplier.delete()
    return redirect("catering_officer_dashboard")

@login_required
def add_inventory(request):
    if request.method == "POST":
        ingredient_id = request.POST.get("ingredient")  # Get ingredient ID from form
        ingredient = get_object_or_404(Ingredient, id=ingredient_id)  # Convert ID to instance

        quantity = request.POST.get("quantity")
        expiry_date = request.POST.get("expiry_date")
        price = request.POST.get("price")
        location = request.POST.get("location")
        category = request.POST.get("category")
        status = request.POST.get("status")

        # Create new inventory item with all required fields
        Inventory.objects.create(
            ingredient=ingredient,
            quantity=quantity,
            expiry_date=expiry_date,
            price=price,
            location=location,
            category=category,
            status=status
        )

    return redirect("storekeeper_dashboard")

@login_required
def edit_inventory(request, item_id):
    item = get_object_or_404(Inventory, id=item_id)
    if request.method == "POST":
        item.ingredient.name = request.POST["ingredient"]
        item.quantity = request.POST["quantity"]
        item.expiry_date = request.POST["expiry_date"]
        item.save()
    return redirect("storekeeper_dashboard")

@login_required
def delete_inventory(request, item_id):
    item = get_object_or_404(Inventory, id=item_id)
    item.delete()
    return redirect("storekeeper_dashboard")

                                    

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
# @user_passes_test(is_storekeeper)
def storekeeper_dashboard(request):
    return render(request, 'accounts/storekeeper_dashboard.html')

@login_required
# @user_passes_test(is_catering_officer)
def catering_officer_dashboard(request):
    return render(request, 'accounts/catering_officer_dashboard.html')

@login_required
# @user_passes_test(is_assistant_catering_officer)
def assistant_catering_officer_dashboard(request):
    return render(request, 'accounts/assistant_catering_officer_dashboard.html')

@login_required
def default_dashboard(request):
    return render(request, 'accounts/default_dashboard.html')

def storekeeper_dashboard(request):



    inventory = Inventory.objects.all()
    ingredients = Ingredient.objects.all()  # This retrieves all ingredients

    context = {
        'inventory': inventory,
        'ingredients': ingredients,
    }

    return render(request, 'accounts/storekeeper_dashboard.html', context)  

def catering_officer_dashboard(request):
    # Fetch necessary data
    inventory = Inventory.objects.all()
    ingredients = Ingredient.objects.all()
    orders = Order.objects.all()
    suppliers = Supplier.objects.all()

    context = {
        'inventory': inventory,
        'ingredients': ingredients,
        'orders': orders,
        'suppliers': suppliers,
    }
    return render(request, 'accounts/catering_officer_dashboard.html', context)

def assistant_catering_dashboard(request):

    context = {
        'ingredients': Ingredient.objects.all()  # This directly passes the queryset to the template
    }

    return render(request, 'accounts/assistant_catering_dashboard.html', context)


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
            if user.groups.filter(name='storekeeper').exists():
                return redirect('storekeeper_dashboard_url')
            elif user.groups.filter(name='catering officer').exists():
                return redirect('catering_officer_dashboard_url')
            elif user.groups.filter(name='assistant catering officer').exists():
                return redirect('assistant_catering_officer_dashboard_url')
            else:
                return redirect('default_dashboard')  # Default if no group assigned

        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})

    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


# Home page view
def home(request):
    inventory = Inventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {'inventory': inventory})

