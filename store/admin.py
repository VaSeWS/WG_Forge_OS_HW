from django.contrib import admin

from .models import Author, Genre, Publisher, Book, Order, OrderEntry


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(OrderEntry)
