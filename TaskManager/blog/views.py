from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Comment, Category
from .forms import CommentForm


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'post_list.html'


def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, template_name="post_list.html", context=context)


# def post_detail(request, year, month, day, post):
#     form = CommentForm()
#     if request.method == 'POSt':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment(
#                 author=form.cleaned_data['author'],
#                 body=form.cleaned_data['body'],
#                 post=post
#             )
#             comment.save()
#     comments = Comment.objects.filter(post=post)
#     post = get_object_or_404(Post,
#                              slug=post,
#                              status='published',
#                              publish__year=year,
#                              publish__month=month,
#                              publish__day=day)
#     context = {
#         "post": post,
#         "comments": comments,
#         "form": form
#     }
#
#     return render(request, "post_detail.html", context=context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    context = {
        "post": post,
    }
    return render(request, 'post_detail.html', context=context)


def blog_category(request, category):
    posts = Post.objects.filter(
        category__name__context=category
    ).order_by('created_on')
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, template_name='post_category.html', context=context)
