from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                count += 1
                form.cleaned_data
        if count > 1:
            raise ValidationError('Основной раздел должен быть один!')

        if count < 1:
            raise ValidationError('Выберете один основной раздел!')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ('id', 'text', 'published_at', 'image')

    
@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')

    
    
    

