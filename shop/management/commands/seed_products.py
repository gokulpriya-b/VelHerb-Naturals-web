from django.core.management.base import BaseCommand
from shop.models import Product
class Command(BaseCommand):
    help = "Create starter VelHerb products if the catalogue is empty."
    def handle(self, *args, **kwargs):
        products = [
            ("VelHerb Herbal Soap","herbal-soap","Bath & Body","A gentle handmade herbal bathing bar.", "Aloe vera, neem leaves, turmeric, coconut oil",149,"soap.jpg",True),
            ("VelHerb Herbal Face Pack","herbal-face-pack","Skin Care","Traditional herbs blended for your self-care ritual.", "Neem, turmeric, sandal powder, kuppaimeni",199,"facepack.jpg",True),
            ("VelHerb Herbal Hair Oil","herbal-hair-oil","Hair Care","A nourishing herbal oil for your hair-care routine.", "Coconut oil, castor oil, hibiscus, amla, fenugreek",249,"hairoil.jpg",True),
            ("VelHerb Javadhu Natural Fragrance","javadhu-fragrance","Fragrance","A traditional natural fragrance inspired by heritage.", "Javadhu powder, botanical fragrance blend",199,"javadhu.jpg",True),
        ]
        if Product.objects.exists():
            self.stdout.write("Products already exist; no changes made.")
            return
        for name, slug, category, short, ingredients, price, image_key, featured in products:
            Product.objects.create(name=name,slug=slug,category=category,short_description=short,
                description=short+" Please check the product label for the final ingredient list and usage directions.",
                ingredients=ingredients,price=price,image_key=image_key,is_featured=featured)
        self.stdout.write(self.style.SUCCESS("Starter VelHerb products created. Update prices and details in Admin."))
