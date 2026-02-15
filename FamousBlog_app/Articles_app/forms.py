from django import forms
from .models import Article
from FamousBlog_app.Categorys_app.models import Category

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'status']  # category та status

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Встановлюємо, щоб в полі Category були всі існуючі категорії
        self.fields['category'].queryset = Category.objects.all()
        # Прибираємо пустий варіант -----
        self.fields['category'].empty_label = None


