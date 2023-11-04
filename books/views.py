from django.shortcuts import render
from django.views import generic
from .models import Book
from django.urls import reverse_lazy, reverse
from .forms import NewBookForm
from django.shortcuts import redirect
from .forms import CommentForm
from .models import Comment
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


@login_required()
def book_create_view(request,):
    if request.method == 'POST':
        form = NewBookForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('book_list')
    else:
        form = NewBookForm()
    return render(request, 'books/book_create.html', {'form': form})


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    form_class = NewBookForm
    template_name = 'books/book_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        book_id = int(self.kwargs['pk'])
        book = get_object_or_404(Book, id=book_id)
        obj.book = book

        return super().form_valid(form)
