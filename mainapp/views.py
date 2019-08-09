from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm



# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')


def detail(request, post_id):
    post_detail=get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def result(request):
    post = Post.objects
    return render(request, 'result.html', {'post':post})

def write(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.pub_date = timezone.now()
			post.author = request.user
			post.save()
			return redirect('result')
	else:
		form = PostForm()           
		return render(request, 'write.html', {'form':form})

def delete(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	post.delete()
	return redirect('result')

def edit(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.pub_date = timezone.now()
			post.author = request.user
			post.save()
			return redirect('/detail/'+str(post.id))
	else:
		form=PostForm(instance=post)
		return render(request, 'write.html', {'form':form})

def mypage(request):
	user = request.user
	mypost = Post.objects.filter(author = user)
	mycomment = Comment.objects.filter(author = user)
	return render(request, 'mypage.html', {'mypost' : mypost, 'mycomment' : mycomment})

def review_board(request):
    return render(request, 'review/review_board.html')

def review_detail(request):
    return render(request, 'review/review_detail.html')

def review_write(request):
    return render(request, 'review/review_write.html')

def add_comment(request, post_id):
	post=get_object_or_404(Post, pk=post_id)
	if request.method=='POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.post=post
			comment.author = request.user
			comment.save()
			return redirect('/detail/' + str(post.id))
		else:
			form=CommentForm()
			return render(request, 'add_comment.html', {'form':form})

def delete_comment(request, post_id, comment_id):
	post = get_object_or_404(Post, pk = post_id)
	comment = get_object_or_404(Comment, pk = comment_id)
	if request.method == 'POST':
		comment.delete()
		return redirect('/detail/' + str(post.id))