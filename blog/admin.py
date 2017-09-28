from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post
from .models import Article
from .models import Article2
admin.site.register(Post) #注册模型
# admin.site.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)
admin.site.register(Article2)