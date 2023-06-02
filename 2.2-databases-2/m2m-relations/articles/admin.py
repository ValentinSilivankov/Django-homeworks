from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tag, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    
    def clean(self):
        is_main_count = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    is_main_count += 1
                else:
                    pass
            else:
                pass
        
        if is_main_count == 0:
            raise ValidationError('!!!Добавьте основной раздел!!!')
        elif is_main_count >= 2:
            raise ValidationError('!!!Основной раздел может быть только один!!!')
    
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ArticleScopeInline]

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass