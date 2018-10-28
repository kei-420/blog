from django import forms
from . models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'body',)

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        return title

    def clean_image(self):
        image = self.cleaned_data['image']
        return image

    def clean_body(self):
        body = self.cleaned_data['body']
        return body

    def save(self, commit=True):
        post_info = super(PostForm, self).save(commit=False)
        post_info.user = self._user
        if commit:
            post_info.save()

        return post_info



