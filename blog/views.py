from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post , Comment, Category
from .forms import PostForm, UpdateForm, CommentForm, CategoryForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-created_on']
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        posts = context['posts']

        comments_dict = {}
        for post in posts:
            comments_dict[post.pk] = post.comment_set.all()

        context['comments_dict'] = comments_dict
        return context
    # def get_queryset(self):
    #     return Post.objects.all()

class CommentView(ListView):
    model = Comment
    template_name = 'blog_detail.html'
    context_object_name = 'comments'
    ordering = ['-created_on']

class BlogDeatilView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['all_posts'] = Post.objects.all()        
        context['latest_posts'] = Post.objects.exclude(pk=self.object.pk).order_by('-created_on')[:5]

        # Add categories to the context
        context['categories'] = self.object.categories.all()

        return context


class CreateBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_blog.html'
    # fields = '__all__'
    # fields = ('title', 'author', 'body')

class UpdateBlogView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_blog.html'

class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')

class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'new_comment.html'
    # fields = '__all__'
    # fields = ('title', 'author', 'body')
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['post_id']
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')

class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'new_category.html'
    success_url = reverse_lazy('categories')

class CategoriesView(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy('categories')

