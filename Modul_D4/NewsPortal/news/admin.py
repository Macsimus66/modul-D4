from django.contrib import admin
from .models import Category
from .models import Post
from .models import Comment
from .models import Author
from .models import PostCategory


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(PostCategory)
