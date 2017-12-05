from django import forms
from my_app.models import Post, Comment

class New_Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'author',
            'title',
            'mess_txt',
        )

    def clean(self):
        cleaned_data = super(New_Post_Form, self).clean()
        author = cleaned_data.get('author')
        post_body = cleaned_data.get('post_body')
        if not author and not post_body:
            raise forms.ValidationError('You have to write something!')

        return cleaned_data


class New_Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'author',
            'comment_body',
        )

    def clean(self):
        cleaned_data = super(New_Comment_Form, self).clean()
        author = cleaned_data.get('author')
        comment_body = cleaned_data.get('comment_body')
        if not author and not comment_body:
            raise forms.ValidationError('You have to write something!')

        return cleaned_data





#    author = forms.CharField(label='Author name', min_length=3)
#    post_body = forms.CharField(
#        widget=forms.Textarea(attrs={'cols': 22, 'rows': 3}),
#        help_text='Post here!',
#        max_length=1000
#    )
#    source = forms.CharField(       # A hidden input for internal use
#        max_length=50,              # tell from which page the user sent the message
#        widget=forms.HiddenInput()
#    )





