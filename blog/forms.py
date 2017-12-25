from django import forms
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from .models import Author, Tag, Category, Post

class AuthorForm(forms.Form):

    class Meta:
        model = Author
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        name_l = name.lower()
        if name_l == "admin" or name_l == "author":
            raise ValidationError("Author name can't be 'admin/author'")
        return name

    def clean_email(self):
        return self.cleaned_data['email'].lower()

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        n = self.cleaned_data['name']
        if n.lower() == "tag" or n.lower() == "add" or n.lower() == "update":
            raise ValidationError("Tag name can't be '{}'".format(n))
        return n

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

    def clean_name(self):
        n = self.cleaned_data['name']
        if n.lower() == "tag" or n.lower() == "add" or n.lower() == "update":
            raise ValidationError("Category name can't be '{}'".format(n))
        return n

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'category', 'tags',)

    def clean_name(self):
        n = self.cleaned_data['title']
        if n.lower() == "post" or n.lower() == "add" or n.lower() == "update":
            raise ValidationError("Post name can't be '{}'".format(n))
        return n

    def save(self):
        instance = super(PostForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()

        return instance