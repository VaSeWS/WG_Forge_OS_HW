from django.views.generic.list import ListView
from .models import Book


class BookListView(ListView):
    model = Book
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

