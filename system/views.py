from django.shortcuts import render

# Create your views here.
def index(request):
    get_data =  Reservation.objects.all()
    context = {'Table_data': get_data}
    return render(request, 'main/index.html', context)

def welcome(request):
    get_data = Reservation.objects.all()
    context = {'Table_data': get_data}
    return render(request, 'main/index,html', context)

def welcome(request):
    return render(request, 'main/welcome.html')

def reservation(request):
    get_the_restuarant = Restaurant.objects.all()
    username = None
    if request.method == 'POST':
        get_number_of_guests = request.POST.get('nmbr_of_guests')
        get_Restaurant_name = request.POST.get('get_restaurant_name')
        get_date = request.POST.get('select_date')
        get_time = request.POST.get('select_time')
        if request.user.is_authenticated:
            username = request.user.username
        try:
            order_exists = Reservation.objects.get(Booking_time = str(get_date) +"T"+ str(get_time), Restaurant__name = get_Restaurant_name)
            return redirect('Booking_Failed')
        except Reservation.DoesNotExist:
            get_restaurant = Restaurant.objects.get(name = get_Restaurant_name)
            create_booking = Reservation.objects.create(Name = username, Restaurant = get_restaurant, Booking_time = get_date +"T"+get_time)
            create_booking.save()
            return redirect('Booking_Successful')
    context = {'restaurant_name': get_the_restuarant}  
    return render(request, 'main/book_your_table.html', context)

def sorry(request):
    return render(request, 'main/sorry.html')

def success(request):
    return render(request, 'main/success.html')