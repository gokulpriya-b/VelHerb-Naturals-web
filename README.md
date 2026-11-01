# VelHerb Naturals — Full-stack Django website

A premium, responsive herbal-products storefront built with Python + Django, SQLite, HTML, CSS and JavaScript.

## Included
- Animated first-visit brand intro / logo reveal
- Premium green, ivory and gold storefront
- Product catalogue and product detail pages
- Add-to-cart and checkout flow
- Custom herbal order form
- Admin dashboard with new-order polling and notification sound
- FAQ-style chat assistant
- Django admin for managing products and orders
- Uploaded VelHerb logo and product images

## Run on Windows (CMD)
1. Install Python 3.11 or 3.12.
2. Extract this ZIP.
3. Open CMD inside the extracted `velherb_naturals_fullstack` folder.
4. Run:

```cmd
py -m venv env
env\Scripts\activate
python -m pip install -r requirements.txt
python manage.py makemigrations shop
python manage.py migrate
python manage.py seed_products
python manage.py createsuperuser
python manage.py runserver
```

5. Open http://127.0.0.1:8000/
6. Admin: http://127.0.0.1:8000/admin/

## Admin order alerts
Log in at `/admin/` and open `/staff/orders/` in the same browser. Keep that dashboard open. When a new order arrives, it polls the server and plays a short notification tone. Browsers require a user interaction before sound can play, so click **Enable sound** once.

## Important before real business use
- Product prices, weights, ingredient lists, stock and contact details are demo values. Edit them in Django Admin.
- Configure a real email/SMS/WhatsApp provider for alerts outside the admin browser.
- Add a payment gateway only after creating merchant credentials and testing its webhook flow.
- Add shipping, privacy, returns and terms pages before public launch.
- Do not publish medical or guaranteed skin/hair treatment claims without suitable evidence and regulatory review.
