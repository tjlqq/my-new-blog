from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     paginator = Paginator(posts, 1)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#        posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post_list.html',{'posts':posts})
USER_LIST = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
def post_list(request):
    # 每页显示10条数据
    per_page_count = 1
    # current-page 当有页
    current_page = request.GET.get('p')
    if current_page == None:
        current_page = 1
    else:
        # 数字运算要转成int类型
        current_page = int(current_page)
    # 如果是第1页，索引0-9，就是1-10的数
    # p=1
    # 0,10   0-9  取索引
    # p=2
    # 大于等于10，小于20就是10-19
    # 10,20 10-19
    # start 开始页数  end=结束页数

    # 如果p=1-1=0
    start = (current_page - 1) * per_page_count
    # 1 * 10=10
    end = current_page * per_page_count
    # 数据切片，每次显示10页
    data = USER_LIST[start:end]

    # 上一页
    prev_pager = current_page - 1
    if prev_pager == 0:
    # 下一页
        prev_pager = 1
        next_pager = current_page + 1
        return render(request, 'blog/post_list.html', {'user_list': data, 'prev_pager': prev_pager, 'next_pager': next_pager})
    else:
        prev_pager = prev_pager = current_page - 1
        next_pager = current_page + 1
        return render(request, 'blog/post_list.html', {'user_list': data, 'prev_pager': prev_pager, 'next_pager': next_pager})
def post_detail(request, pk):
    current_page = request.GET.get('p')
    if current_page == None:
        current_page = 1
    else:
        # 数字运算要转成int类型
        current_page = int(current_page)
    prev_pager = current_page -1
    next_pager = current_page +1
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post,'prev_pager': prev_pager, 'next_pager': next_pager})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def index(request):
    return render(request,'blog/index.html')