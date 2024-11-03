from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order

def create_client(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        client = Client.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect('client_list')
    return render(request, 'shop/create_client.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'shop/client_list.html', {'clients': clients})

def update_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.name = request.POST['name']
        client.email = request.POST['email']
        client.phone = request.POST['phone']
        client.address = request.POST['address']
        client.save()
        return redirect('client_list')
    return render(request, 'shop/update_client.html', {'client': client})

def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'shop/delete_client.html', {'client': client})

def home(request):
    clients = Client.objects.all()  # Загрузка всех клиентов
    products = Product.objects.all()  # Загрузка всех товаров
    orders = Order.objects.all()  # Загрузка всех заказов
    return render(request, 'shop/home.html', {'clients': clients, 'products': products, 'orders': orders})
