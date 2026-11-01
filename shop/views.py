import json
from decimal import Decimal, InvalidOperation
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Product, Order, CustomOrder

def home(request):
    featured = Product.objects.filter(is_available=True, is_featured=True)[:4]
    if not featured.exists(): featured = Product.objects.filter(is_available=True)[:4]
    return render(request, "shop/home.html", {"featured": featured})

def products(request):
    qs = Product.objects.filter(is_available=True)
    category = request.GET.get("category", "")
    if category: qs = qs.filter(category__iexact=category)
    return render(request, "shop/products.html", {"products": qs, "category": category})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, "shop/product_detail.html", {"product": product})

def custom_order(request):
    if request.method == "POST":
        data = request.POST
        required = ["customer_name", "phone", "product_type"]
        if not all(data.get(x, "").strip() for x in required):
            messages.error(request, "Please fill in your name, phone number and product type.")
        else:
            CustomOrder.objects.create(
                customer_name=data["customer_name"].strip(), phone=data["phone"].strip(),
                email=data.get("email","").strip(), product_type=data["product_type"].strip(),
                ingredients_requested=data.get("ingredients_requested","").strip(),
                quantity=max(1, int(data.get("quantity") or 1)),
                budget=data.get("budget","").strip(), notes=data.get("notes","").strip())
            messages.success(request, "Your custom order request has been received. Our team will contact you.")
            return redirect("custom_order")
    return render(request, "shop/custom_order.html")

def checkout(request):
    if request.method == "POST":
        try:
            cart = json.loads(request.POST.get("cart_json", "[]"))
            if not cart: raise ValueError("Your cart is empty.")
            summaries, total = [], Decimal("0.00")
            for item in cart:
                product = get_object_or_404(Product, pk=int(item["id"]), is_available=True)
                qty = max(1, min(99, int(item["qty"])))
                line = product.price * qty
                total += line
                summaries.append(f"{product.name} × {qty} — ₹{line}")
            order = Order.objects.create(
                customer_name=request.POST["customer_name"].strip(),
                phone=request.POST["phone"].strip(), email=request.POST.get("email","").strip(),
                address=request.POST["address"].strip(), items="\\n".join(summaries), total=total)
            return redirect("order_success", order_id=order.id)
        except (ValueError, KeyError, TypeError, InvalidOperation, json.JSONDecodeError):
            messages.error(request, "Please check your cart and customer details.")
    return render(request, "shop/checkout.html")

def order_success(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, "shop/order_success.html", {"order": order})

@staff_member_required
def staff_orders(request):
    return render(request, "shop/staff_orders.html", {
        "orders": Order.objects.order_by("-created_at")[:30],
        "custom_orders": CustomOrder.objects.order_by("-created_at")[:30],
        "latest_order_id": Order.objects.order_by("-id").values_list("id", flat=True).first() or 0,
        "latest_custom_id": CustomOrder.objects.order_by("-id").values_list("id", flat=True).first() or 0,
    })

@staff_member_required
def order_feed(request):
    after = int(request.GET.get("after_order", "0"))
    after_custom = int(request.GET.get("after_custom", "0"))
    orders = list(Order.objects.filter(id__gt=after).order_by("id").values(
        "id","customer_name","phone","total","created_at","is_custom"))
    customs = list(CustomOrder.objects.filter(id__gt=after_custom).order_by("id").values(
        "id","customer_name","phone","product_type","created_at"))
    return JsonResponse({"orders": orders, "custom_orders": customs})
