from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=50,
    )
    surname = models.CharField(
        max_length=50,
    )
    patronymic = models.CharField(
        blank=True,
        max_length=50,
    )
    bio = models.TextField(
        blank=True,
        max_length=500,
    )
    portrait = models.ImageField(
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return ' '.join((self.name, self.surname))


class Genre(models.Model):
    name = models.CharField(
        max_length=70,
    )
    description = models.TextField(
        max_length=200,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(
        max_length=50,
    )
    description = models.TextField(
        blank=True,
        max_length=300,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.RESTRICT,
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.RESTRICT,
    )
    title = models.CharField(
        unique=True,
        max_length=100,
    )
    description = models.TextField(
        blank=True,
        max_length=500,
    )
    image = models.ImageField(
        blank=True,
    )
    date_written = models.DateField()
    pages_amount = models.PositiveSmallIntegerField()
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.RESTRICT,
    )
    date_published = models.DateField()
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


class Order(models.Model):
    address = models.TextField(
        max_length=300
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )


class OrderEntry(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.SET("Deleted book price"),
    )
    amount = models.PositiveSmallIntegerField()
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
