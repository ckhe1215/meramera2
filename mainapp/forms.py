from django import forms
from .models import Post, Comment, Complaint


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','image','body','rent_date','price','choice_parcel','use','region_sido','region_sigungu','region_rest','sort',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'is_secret', 'is_accepted')

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('title','author','text','pub_date')

        
# class SearchForm(forms.Form):
#     schWord = forms.CharField(label='Search Word')