from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
import io
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
import random
# from .utlis import send_code
import uuid
from itertools import chain


def home_view(request):
    menproducts = models.Product.objects.filter(gender="Men")
    womenproducts = models.Product.objects.filter(gender="Women")
    products = models.Product.objects.all()
    cart = {}
    total_price = 0
    product_count_in_cart = 0
    product_count_in_wishlist = 0
    newest = random.sample(list(products), min(2, len(products)))
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    else:
        return render(request, 'index-10.html', {'cart': cart, 'total_price': total_price, 'products': products, 'product_count_in_cart': product_count_in_cart, 'men': menproducts, 'women': womenproducts, 'product_count_in_wishlist': product_count_in_wishlist, 'newest': newest})


def products(request):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    products = models.Product.objects.all()
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)
        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            total_price += ca.quantity*ca.get_price
            product_count_in_cart += ca.quantity

    # if 'product_ids' in request.COOKIES:
    #     product_ids = request.COOKIES['product_ids']
    #     counter = product_ids.split('|')
    #     product_count_in_cart = len(set(counter))
    # else:
    #     product_count_in_cart = 0
    return render(request, 'category.html', {'url': "all", 'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist, 'total_price': total_price})


def hightolow(request, id):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0
    if id == "all":
        products = models.Product.objects.all().order_by("-price")
    else:
        products = models.Product.objects.filter(
            tag1__icontains=id).order_by("-price")
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)

        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            product_count_in_cart += ca.quantity

    return render(request, 'category.html', {'url': id, 'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


def productmen(request):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0

    products = models.Product.objects.filter(gender='Men')
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)

        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            product_count_in_cart += ca.quantity

    return render(request, 'category.html', {'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


def productwomen(request):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0

    products = models.Product.objects.filter(gender='Women')
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)

        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            product_count_in_cart += ca.quantity

    return render(request, 'category.html', {'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


def producttshirt(request):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0
    url = "tshirt"
    products = models.Product.objects.filter(tag1__icontains="tshirt")
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)

        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            product_count_in_cart += ca.quantity

    return render(request, 'category.html', {'url': url, 'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


def producthoodie(request):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0
    url = "hoodie"
    products = models.Product.objects.filter(tag1__icontains="hoodie")
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)

        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            product_count_in_cart += ca.quantity

    return render(request, 'category.html', {'url': url, 'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


def productcap(request):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0
    url = "cap"
    products = models.Product.objects.filter(tag1__icontains="cap")
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)

        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            product_count_in_cart += ca.quantity

    return render(request, 'category.html', {'url': url, 'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


def productartistic(request):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0
    url = "artistic"
    products = models.Product.objects.filter(tag1__icontains="artistic")
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)

        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            product_count_in_cart += ca.quantity

    return render(request, 'category.html', {'url': url, 'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


def productbracelet(request):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0
    url = "bracelet"
    products = models.Product.objects.filter(tag1__icontains="bracelet")
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)

        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            product_count_in_cart += ca.quantity

    return render(request, 'category.html', {'url': url, 'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


def productkeychain(request):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0
    url = "keychain"
    products = models.Product.objects.filter(tag1__icontains="keychain")
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)

        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            product_count_in_cart += ca.quantity

    return render(request, 'category.html', {'url': url, 'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


def productcategory(request):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)

        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            product_count_in_cart += ca.quantity

    # if 'product_ids' in request.COOKIES:
    #     product_ids = request.COOKIES['product_ids']
    #     counter = product_ids.split('|')
    #     product_count_in_cart = len(set(counter))
    # else:
    #     product_count_in_cart = 0
    return render(request, 'product-category-boxed.html', {'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


def lowtohigh(request, id):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0

    if id == "all":
        products = models.Product.objects.all().order_by("price")
    else:
        products = models.Product.objects.filter(
            tag1__icontains=id).order_by("price")
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)

        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            product_count_in_cart += ca.quantity

    # if 'product_ids' in request.COOKIES:
    #     product_ids = request.COOKIES['product_ids']
    #     counter = product_ids.split('|')
    #     product_count_in_cart = len(set(counter))
    # else:
    #     product_count_in_cart = 0
    return render(request, 'category.html', {'url': id, 'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


def between(request):
    products = models.Product.objects.all()
    ans = []
    if request.method == 'POST':
        low = request.POST['low']
        high = request.POST['high']
        low = int(low)
        high = int(high)
        if low > high:
            kl = high
            high = low
            low = kl

        for ui in products:
            print(type(ui.price))
            print(type(low))
            if int(ui.price) >= low and int(ui.price) <= high:
                ans.append(ui)
        products = ans
    customer = models.Customer.objects.get(user=request.user)
    cart = models.Cart.objects.filter(customer=customer)
    wishlist = models.Wishlist.objects.filter(customer=customer)
    product_count_in_cart = 0
    product_count_in_wishlist = len(wishlist)
    for ca in cart:
        product_count_in_cart += ca.quantity

    return render(request, 'category.html', {'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


# for showing login button for admin(by sumit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


@login_required(login_url='/loginuser')
def logout(request):
    auth.logout(request)
    messages.success(request, "Succesfully logout")
    return redirect("/")


@login_required(login_url='/loginuser')
def checkout(request):
    custom = models.Customer.objects.get(user=request.user)
    cart = models.Cart.objects.all().filter(customer=custom)
    total = 0
    product_count_in_cart = 0
    total_price = 0
    for ca in cart:
        total_price += ca.quantity*ca.get_price
        product_count_in_cart += ca.quantity

    return render(request, 'checkout.html', {'customer': custom, 'total_price': total_price, 'product': products, 'cart': cart, 'total': total, 'product_count_in_cart': product_count_in_cart})


def loginuser(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    if request.method == 'POST':
        username = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if username is not None and password is not None:
            profile_obj = models.Customer.objects.filter(user=user).first()
            if user is not None and profile_obj.is_active:
                auth.login(request, user)
                messages.info(request, "Successfully logged in!")
                return redirect('/')
            if user is not None:

                messages.success(
                    request, 'You need to verify your account .Kindly check your email ')
                return redirect('/')
            else:
                messages.info(request, "invalid credentials")
                return redirect('/')
    else:
        return render(request, 'login.html')


def customer_signup_view(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request, 'ecom/customersignup.html', context=mydict)

# -----------for checking user iscustomer


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        passs = request.POST['password']
        pass2 = request.POST['password2']
        mobile = request.POST['mobile']
        address = request.POST['address']
        image = request.FILES.get('image')
        if passs == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(
                    request, 'Email already taken. Please login !!!!')
                return redirect('/')
            elif User.objects.filter(username=username).exists():
                messages.info(
                    request, 'Username already taken . Please try another !!!!')
                return redirect('/')
            else:

                token = str(uuid.uuid4())
                print(token)
                send_mail_after_registration(email, token)
                user = User.objects.create_user(
                    username=username, email=email, password=passs, first_name=firstname, last_name=lastname)
                user.save()
                profile = models.Customer.objects.create(is_active=False,
                                                         profile_pic=image, token=token, user=user, address=address, mobile=mobile)
                profile.save()
                my_customer_group = Group.objects.get_or_create(
                    name='CUSTOMER')
                my_customer_group[0].user_set.add(user)
                # us = auth.authenticate(username=username, password=passs)
                # auth.login(request, us)
                # userr = User.objects.get(username=username)

                messages.success(
                    request, 'Verify your account from your email')
                return redirect('/')
        else:
            messages.info(request, 'Enter same password in both')
            return redirect('/')

    return redirect('/')


def send_mail_after_registration(email, token):
    print("Done>>>>>")
    subject = 'Your accounts need to be verified'
    message = f'Thank you for signing up on our platform.Kindly click the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def verify(request, auth_token):
    try:
        profile_obj = models.Customer.objects.filter(token=auth_token).first()
        if profile_obj.is_active:
            messages.success(request, 'Your account is already verified ')
            return redirect('/loginuser')
        if profile_obj:
            profile_obj.is_active = True
            profile_obj.save()
            messages.success(request, 'Your account is verified ')
            return redirect('/loginuser')
        else:
            return redirect('/')
    except Exception as e:
        print(e)


def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()


# ---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,CUSTOMER
def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('customer-home')
    else:
        return redirect('admin-dashboard')

# ---------------------------------------------------------------------------------
# ------------------------ ADMIN RELATED VIEWS START ------------------------------
# ---------------------------------------------------------------------------------


@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    # for cards on dashboard
    customercount = models.Customer.objects.all().count()
    productcount = models.Product.objects.all().count()
    ordercount = models.Orders.objects.all().count()

    # for recent order tables
    orders = models.Orders.objects.all()
    ordered_products = []
    ordered_bys = []
    for order in orders:
        ordered_product = models.Product.objects.all().filter(id=order.product.id)
        ordered_by = models.Customer.objects.all().filter(id=order.customer.id)
        ordered_products.append(ordered_product)
        ordered_bys.append(ordered_by)

    mydict = {
        'customercount': customercount,
        'productcount': productcount,
        'ordercount': ordercount,
        'data': zip(ordered_products, ordered_bys, orders),
    }
    return render(request, 'ecom/admin_dashboard.html', context=mydict)


# admin view customer table
@login_required(login_url='adminlogin')
def view_customer_view(request):
    customers = models.Customer.objects.all()
    return render(request, 'ecom/view_customer.html', {'customers': customers})

# admin delete customer


@login_required(login_url='adminlogin')
def delete_customer_view(request, pk):
    customer = models.Customer.objects.get(id=pk)
    user = models.User.objects.get(id=customer.user_id)

    user.delete()
    customer.delete()
    return redirect('view-customer')


@login_required(login_url='loginuser')
def addreview(request, pk):
    customer = models.Customer.objects.get(user=request.user)
    products = models.Product.objects.get(id=int(pk))
    if request.method == 'POST':
        rating = request.POST['rating']
        review = request.POST['review']
        title = request.POST['title']
        feedback = models.Feedback.objects.create(
            product=products, customer=customer, feedback=review, rating=rating, title=title)
        feedback.save()
        # print(feedback)
        return redirect("/productdetail/"+pk)
    return redirect("/productdetail/"+pk)


@login_required(login_url='adminlogin')
def update_customer_view(request, pk):
    customer = models.Customer.objects.get(id=pk)
    user = models.User.objects.get(id=customer.user_id)
    userForm = forms.CustomerUserForm(instance=user)
    customerForm = forms.CustomerForm(request.FILES, instance=customer)
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST, instance=user)
        customerForm = forms.CustomerForm(request.POST, instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return redirect('view-customer')
    return render(request, 'ecom/admin_update_customer.html', context=mydict)

# admin view the product


@login_required(login_url='adminlogin')
def admin_products_view(request):
    products = models.Product.objects.all()
    return render(request, 'ecom/admin_products.html', {'products': products})


# admin add product by clicking on floating button
@login_required(login_url='adminlogin')
def admin_add_product_view(request):
    productForm = forms.ProductForm()
    if request.method == 'POST':
        productForm = forms.ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
        return HttpResponseRedirect('admin-products')
    return render(request, 'ecom/admin_add_products.html', {'productForm': productForm})


@login_required(login_url='adminlogin')
def delete_product_view(request, pk):
    product = models.Product.objects.get(id=pk)
    product.delete()
    return redirect('admin-products')


@login_required(login_url='adminlogin')
def update_product_view(request, pk):
    product = models.Product.objects.get(id=pk)
    productForm = forms.ProductForm(instance=product)
    if request.method == 'POST':
        productForm = forms.ProductForm(
            request.POST, request.FILES, instance=product)
        if productForm.is_valid():
            productForm.save()
            return redirect('admin-products')
    return render(request, 'ecom/admin_update_product.html', {'productForm': productForm})


@login_required(login_url='adminlogin')
def admin_view_booking_view(request):
    orders = models.Orders.objects.all()
    ordered_products = []
    ordered_bys = []
    for order in orders:
        ordered_product = models.Product.objects.all().filter(id=order.product.id)
        ordered_by = models.Customer.objects.all().filter(id=order.customer.id)
        ordered_products.append(ordered_product)
        ordered_bys.append(ordered_by)
    return render(request, 'ecom/admin_view_booking.html', {'data': zip(ordered_products, ordered_bys, orders)})


@login_required(login_url='adminlogin')
def delete_order_view(request, pk):
    order = models.Orders.objects.get(id=pk)
    order.delete()
    return redirect('admin-view-booking')

# for changing status of order (pending,delivered...)


@login_required(login_url='adminlogin')
def update_order_view(request, pk):
    order = models.Orders.objects.get(id=pk)
    orderForm = forms.OrderForm(instance=order)
    if request.method == 'POST':
        orderForm = forms.OrderForm(request.POST, instance=order)
        if orderForm.is_valid():
            orderForm.save()
            return redirect('admin-view-booking')
    return render(request, 'ecom/update_order.html', {'orderForm': orderForm})


# admin view the feedback
@login_required(login_url='adminlogin')
def view_feedback_view(request):
    feedbacks = models.Feedback.objects.all().order_by('-id')
    return render(request, 'ecom/view_feedback.html', {'feedbacks': feedbacks})


# ---------------------------------------------------------------------------------
# ------------------------ PUBLIC CUSTOMER RELATED VIEWS START ---------------------
# ---------------------------------------------------------------------------------
def search_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    products = models.Product.objects.all().filter(tag1__icontains=query)
    # products1 = models.Product.objects.all().filter(tag1__icontains=query)
    # products2 = models.Product.objects.all().filter(tag2__icontains=query)
    # products3 = models.Product.objects.all().filter(gender__icontains=query)
    # products = list(chain(products, products1))
    # products = list(chain(products, products2))
    # products = list(chain(products, products3))
    # products = set(products)
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0

    words = "searched Results:"
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.filter(customer=customer)
        wishlist = models.Wishlist.objects.filter(customer=customer)

        product_count_in_wishlist = len(wishlist)
        for ca in cart:
            product_count_in_cart += ca.quantity

    return render(request, 'category.html', {'url': query, 'cart': cart, 'products': products, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': product_count_in_wishlist})


@login_required(login_url="loginuser")
def deletecart(request, id):
    products = models.Product.objects.get(id=id)
    custome = models.Customer.objects.get(user=request.user)
    uu = models.Cart.objects.filter(product=products, customer=custome)
    uu.delete()
    print(request.path_info)
    return redirect("/cart")

# any one can add product to cart, no need of signin


def product_detail(request, pk):
    cart = {}
    wishlist = {}
    product_count_in_cart = 0
    total_price = 0
    product_count_in_wishlist = 0
    total = 0
    productss = models.Product.objects.all().exclude(id=pk)
    products = models.Product.objects.get(id=pk)
    randomproducts = random.sample(list(productss), min(5, len(productss)))

    review = models.Feedback.objects.filter(product=products)
    if request.user.is_authenticated:
        custom = models.Customer.objects.get(user=request.user)
        cart = models.Cart.objects.all().filter(customer=custom)
        wishlist = models.Wishlist.objects.filter(customer=custom)

        for ca in cart:
            total_price += ca.quantity*ca.get_price
            product_count_in_cart += ca.quantity
    return render(request, 'product-centered.html', {'randomproducts': randomproducts, 'total_price': total_price,  "review": review, "noofreview": len(review), 'product': products, 'cart': cart, 'total': total, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': len(wishlist)})


@login_required(login_url="loginuser")
def add_to_cart_view(request, pk):
    products = models.Product.objects.get(id=pk)
    custome = models.Customer.objects.get(user=request.user)
    if models.Cart.objects.filter(product=products, customer=custome).exists():
        uu = models.Cart.objects.get(product=products, customer=custome)
        uu.quantity = uu.quantity+1
        uu.save()
    else:
        yu = models.Cart.objects.create(
            customer=custome, product=products, quantity=1)
        yu.save()
    # for cart counter, fetching products ids added by customer from cookies
    # if 'product_ids' in request.COOKIES:
    #     product_ids = request.COOKIES['product_ids']
    #     counter = product_ids.split('|')
    #     product_count_in_cart = len(set(counter))
    # else:
    #     product_count_in_cart = 1

    # response = render(request, 'category.html',
    #                   {'products': products, 'product_count_in_cart': product_count_in_cart})

    # # adding product id to cookies
    # if 'product_ids' in request.COOKIES:
    #     product_ids = request.COOKIES['product_ids']
    #     if product_ids == "":
    #         product_ids = str(pk)
    #     else:
    #         product_ids = product_ids+"|"+str(pk)
    #     response.set_cookie('product_ids', product_ids)
    # else:
    #     response.set_cookie('product_ids', pk)

    # product = models.Product.objects.get(id=pk)
    messages.info(request, products.name + ' added to cart successfully!')

    return redirect("/cart")


@login_required(login_url="loginuser")
def remove_one(request, pk):
    products = models.Product.objects.get(id=pk)
    custome = models.Customer.objects.get(user=request.user)
    if models.Cart.objects.filter(product=products, customer=custome).exists():
        uu = models.Cart.objects.get(product=products, customer=custome)
        uu.quantity = uu.quantity-1
        if uu.quantity == 0:
            uu.delete()
        else:
            uu.save()

    # messages.info(request, products.name + ' added to cart successfully!')

    return redirect("/cart")


@login_required(login_url="loginuser")
def add_to_wishlist(request, pk):
    products = models.Product.objects.get(id=pk)
    custome = models.Customer.objects.get(user=request.user)
    if models.Wishlist.objects.filter(product=products, customer=custome).exists():
        pass
    else:
        yu = models.Wishlist.objects.create(
            customer=custome, product=products)
        yu.save()

    messages.info(request, products.name + ' added to wishlist successfully!')

    return redirect("/wishlist")


# for checkout of cart
@login_required(login_url="loginuser")
def cart_view(request):
    # for cart counter
    custom = models.Customer.objects.get(user=request.user)
    cart = models.Cart.objects.all().filter(customer=custom)
    wishlist = models.Wishlist.objects.filter(customer=custom)
    total = 0
    product_count_in_cart = 0
    total_price = 0
    for ca in cart:
        total_price += ca.quantity*ca.get_price
        product_count_in_cart += ca.quantity

    # if 'product_ids' in request.COOKIES:
    #     product_ids = request.COOKIES['product_ids']
    #     counter = product_ids.split('|')
    #     product_count_in_cart = len(set(counter))
    # else:
    #     product_count_in_cart = 0

    # # fetching product details from db whose id is present in cookie
    # products = None
    # total = 0
    # if 'product_ids' in request.COOKIES:
    #     product_ids = request.COOKIES['product_ids']
    #     if product_ids != "":
    #         product_id_in_cart = product_ids.split('|')
    #         products = models.Product.objects.all().filter(id__in=product_id_in_cart)
    #         # for total price shown in cart
    #         for p in products:
    #             total = total+p.price
    return render(request, 'cart.html', {'total_price': total_price, 'product': products, 'cart': cart, 'total': total, 'product_count_in_cart': product_count_in_cart, 'product_count_in_wishlist': len(wishlist)})


@login_required(login_url="loginuser")
def wishlist(request):
    # for cart counter
    custom = models.Customer.objects.get(user=request.user)
    cart = models.Cart.objects.all().filter(customer=custom)
    wishlist = models.Wishlist.objects.all().filter(customer=custom)
    total = 0
    product_count_in_wishlist = len(wishlist)
    return render(request, 'wishlist.html', {'wishlist': wishlist, 'cart': cart, 'product_count_in_cart': len(cart), 'product_count_in_wishlist': product_count_in_wishlist})


@login_required(login_url="loginuser")
def helpful(request, kl, pk):
    review = models.Feedback.objects.get(id=pk)
    customer = models.Customer.objects.get(user=request.user)
    products = models.Product.objects.get(id=kl)
    if models.Like.objects.filter(review=review, customer=customer).exists():
        like = models.Like.objects.get(review=review, customer=customer)
        review.helpful -= 1
        review.save()
        like.delete()
    else:
        like = models.Like.objects.create(
            product=products, review=review, customer=customer)
        review.helpful += 1
        review.save()
        like.save()
    return redirect("/productdetail/"+kl)
    # custom = models.Customer.objects.get(user=request.user)
    # cart = models.Cart.objects.all().filter(customer=custom)
    # wishlist = models.Wishlist.objects.all().filter(customer=custom)
    # total = 0
    # product_count_in_wishlist = len(wishlist)
    # return render(request, 'wishlist.html', {'wishlist': wishlist, 'cart': cart, 'product_count_in_wishlist': product_count_in_wishlist})


def remove_from_cart_view(request, pk):
    # for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    # removing product id from cookie
    total = 0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        product_id_in_cart = product_ids.split('|')
        product_id_in_cart = list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products = models.Product.objects.all().filter(id__in=product_id_in_cart)
        # for total price shown in cart after removing product
        for p in products:
            total = total+p.price

        #  for update coookie value after removing product id in cart
        value = ""
        for i in range(len(product_id_in_cart)):
            if i == 0:
                value = value+product_id_in_cart[0]
            else:
                value = value+"|"+product_id_in_cart[i]
        response = render(request, 'ecom/cart.html', {
                          'products': products, 'total': total, 'product_count_in_cart': product_count_in_cart})
        if value == "":
            response.delete_cookie('product_ids')
        response.set_cookie('product_ids', value)
        return response


def send_feedback_view(request):
    feedbackForm = forms.FeedbackForm()
    if request.method == 'POST':
        feedbackForm = forms.FeedbackForm(request.POST)
        if feedbackForm.is_valid():
            feedbackForm.save()
            return render(request, 'ecom/feedback_sent.html')
    return render(request, 'ecom/send_feedback.html', {'feedbackForm': feedbackForm})


# ---------------------------------------------------------------------------------
# ------------------------ CUSTOMER RELATED VIEWS START ------------------------------
# ---------------------------------------------------------------------------------
@login_required(login_url='loginuser')
@csrf_exempt
@user_passes_test(is_customer)
def customer_home_view(request):
    menproducts = models.Product.objects.filter(gender="Men")
    womenproducts = models.Product.objects.filter(gender="Women")
    products = models.Product.objects.all()
    customer = models.Customer.objects.get(user=request.user)
    cart = models.Cart.objects.filter(customer=customer)
    wishlist = models.Wishlist.objects.filter(customer=customer)
    product_count_in_cart = 0
    newest = models.Product.objects.order_by('-date')
    product_count_in_wishlist = len(wishlist)
    total_price = 0

    for ca in cart:
        total_price += ca.quantity*ca.get_price
        product_count_in_cart += ca.quantity

    return render(request, 'index-10.html', {'newest': newest, 'cart': cart, 'total_price': total_price, 'products': products, 'product_count_in_cart': product_count_in_cart, 'men': menproducts, 'women': womenproducts, 'product_count_in_wishlist': product_count_in_wishlist})


# shipment address before placing order
@login_required(login_url='customerlogin')
def customer_address_view(request):
    # this is for checking whether product is present in cart or not
    # if there is no product in cart we will not show address form
    product_in_cart = False
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_in_cart = True
    # for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 0

    addressForm = forms.AddressForm()
    if request.method == 'POST':
        addressForm = forms.AddressForm(request.POST)
        if addressForm.is_valid():
            # here we are taking address, email, mobile at time of order placement
            # we are not taking it from customer account table because
            # these thing can be changes
            email = addressForm.cleaned_data['Email']
            mobile = addressForm.cleaned_data['Mobile']
            address = addressForm.cleaned_data['Address']
            # for showing total price on payment page.....accessing id from cookies then fetching  price of product from db
            total = 0
            if 'product_ids' in request.COOKIES:
                product_ids = request.COOKIES['product_ids']
                if product_ids != "":
                    product_id_in_cart = product_ids.split('|')
                    products = models.Product.objects.all().filter(id__in=product_id_in_cart)
                    for p in products:
                        total = total+p.price

            response = render(request, 'ecom/payment.html', {'total': total})
            response.set_cookie('email', email)
            response.set_cookie('mobile', mobile)
            response.set_cookie('address', address)
            return response
    return render(request, 'ecom/customer_address.html', {'addressForm': addressForm, 'product_in_cart': product_in_cart, 'product_count_in_cart': product_count_in_cart})


@login_required(login_url="loginuser")
def order(request):
    customer = models.Customer.objects.get(user=request.user)
    if not models.Cart.objects.filter(customer=customer).exists():
        messages.info(request, "Cart empty.Add something")
        return redirect('/products')
    cart = models.Cart.objects.filter(customer=customer)

    email = customer.get_email
    mobile = customer.mobile
    address = customer.address
    for ty in cart:
        prodid = ty.get_id
        product = models.Product.objects.get(id=prodid)
        order = models.Orders.objects.create(
            mobile=mobile, customer=customer, product=product, email=email, address=address, status='Pending', quantity=ty.quantity)
        order.save()
        ty.delete()
    return render(request, 'success.html')

# here we are just directing to this view...actually we have to check whther payment is successful or not
# then only this view should be accessed


@login_required(login_url='customerlogin')
def payment_success_view(request):
    # Here we will place order | after successful payment
    # we will fetch customer  mobile, address, Email
    # we will fetch product id from cookies then respective details from db
    # then we will create order objects and store in db
    # after that we will delete cookies because after order placed...cart should be empty
    customer = models.Customer.objects.get(user_id=request.user.id)
    products = None
    email = None
    mobile = None
    address = None
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart = product_ids.split('|')
            products = models.Product.objects.all().filter(id__in=product_id_in_cart)
            # Here we get products list that will be ordered by one customer at a time

    # these things can be change so accessing at the time of order...
    if 'email' in request.COOKIES:
        email = request.COOKIES['email']
    if 'mobile' in request.COOKIES:
        mobile = request.COOKIES['mobile']
    if 'address' in request.COOKIES:
        address = request.COOKIES['address']

    # here we are placing number of orders as much there is a products
    # suppose if we have 5 items in cart and we place order....so 5 rows will be created in orders table
    # there will be lot of redundant data in orders table...but its become more complicated if we normalize it
    for product in products:
        models.Orders.objects.get_or_create(
            customer=customer, product=product, status='Pending', email=email, mobile=mobile, address=address)

    # after order placed cookies should be deleted
    response = render(request, 'ecom/payment_success.html')
    response.delete_cookie('product_ids')
    response.delete_cookie('email')
    response.delete_cookie('mobile')
    response.delete_cookie('address')
    return response


@login_required(login_url='loginuser')
@user_passes_test(is_customer)
def my_order_view(request):

    customer = models.Customer.objects.get(user_id=request.user.id)
    orders = models.Orders.objects.all().filter(customer_id=customer)
    ordered_products = []
    for order in orders:
        ordered_product = models.Product.objects.all().filter(id=order.product.id)
        ordered_products.append(ordered_product)

    return render(request, 'ecom/my_order.html', {'data': zip(ordered_products, orders)})


# @login_required(login_url='customerlogin')
# @user_passes_test(is_customer)
# def my_order_view2(request):

#     products=models.Product.objects.all()
#     if 'product_ids' in request.COOKIES:
#         product_ids = request.COOKIES['product_ids']
#         counter=product_ids.split('|')
#         product_count_in_cart=len(set(counter))
#     else:
#         product_count_in_cart=0
#     return render(request,'ecom/my_order.html',{'products':products,'product_count_in_cart':product_count_in_cart})

# --------------for discharge patient bill (pdf) download and printing


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return redirect("profile")


@login_required(login_url='loginuser')
@user_passes_test(is_customer)
def invoice(request, pk):
    order = models.Orders.objects.get(id=pk)
    loggedincustomer = models.Customer.objects.get(user=request.user)
    customer = order.customer
    product = order.product
    if loggedincustomer != customer:

        return redirect('/')
    else:
        mydict = {
            'orderDate': order.order_date,
            'customerName': request.user,
            'customerEmail': order.email,
            'customerMobile': order.mobile,
            'shipmentAddress': order.address,
            'orderStatus': order.status,
            'quantity': order.quantity,
            'productName': product.name,
            'productImage': product.product_image,
            'productPrice': product.price,
            'productDescription': product.description,


        }
    return render_to_pdf('ecom/download_invoice.html', mydict)


@login_required(login_url='loginuser')
@user_passes_test(is_customer)
def download_invoice_view(request, orderID, productID):
    order = models.Orders.objects.get(id=orderID)
    product = models.Product.objects.get(id=productID)
    mydict = {
        'orderDate': order.order_date,
        'customerName': request.user,
        'customerEmail': order.email,
        'customerMobile': order.mobile,
        'shipmentAddress': order.address,
        'orderStatus': order.status,

        'productName': product.name,
        'productImage': product.product_image,
        'productPrice': product.price,
        'productDescription': product.description,


    }
    return render_to_pdf('ecom/download_invoice.html', mydict)


def cancel(request, pk):
    order = models.Orders.objects.get(id=pk)
    customer = models.Customer.objects.get(user=request.user)
    if (customer != order.customer):
        messages.info(request, "You have not orderd any such item")
        return redirect("/profile")
    if (order.status == 'Delivered'):
        messages.info(
            request, "Order is already delivered.Try returning the order")
        return redirect("/profile")
    messages.info(
        request, "Order cancelled")
    order.delete()
    return redirect('/profile')


def gh(request):
    return render(request, "product-centered.html")


@login_required(login_url='loginuser')
@user_passes_test(is_customer)
def my_profile_view(request):
    customer = models.Customer.objects.get(user=request.user)
    orders = models.Orders.objects.all().filter(customer=customer)
    wishlist = models.Wishlist.objects.filter(customer=customer)
    cart = models.Cart.objects.filter(customer=customer)

    return render(request, 'website/dashboard.html', {'nooforders': len(orders), 'cart': cart, 'customers': customer, 'orders': orders, 'product_count_in_cart': len(cart), 'product_count_in_wishlist': len(wishlist)})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def edit_profile_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    user = models.User.objects.get(id=customer.user_id)
    userForm = forms.CustomerUserForm(instance=user)
    customerForm = forms.CustomerForm(request.FILES, instance=customer)
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST, instance=user)
        customerForm = forms.CustomerForm(request.POST, instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return HttpResponseRedirect('my-profile')
    return render(request, 'ecom/edit_profile.html', context=mydict)


# ---------------------------------------------------------------------------------
# ------------------------ ABOUT US AND CONTACT US VIEWS START --------------------
# ---------------------------------------------------------------------------------
def aboutus_view(request):
    return render(request, 'ecom/aboutus.html')


def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name = sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email), message, settings.EMAIL_HOST_USER,
                      settings.EMAIL_RECEIVING_USER, fail_silently=False)
            return render(request, 'ecom/contactussuccess.html')
    return render(request, 'ecom/contactus.html', {'form': sub})
