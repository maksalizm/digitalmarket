from django import forms
from .models import Product
from django.utils.text import slugify

PUBLISH_CHOICES = (
    ('publish', "Publish"),
    ('draft', "Draft"),
)


class ProductAddForm(forms.Form):
    title = forms.CharField(label="Your title", widget=forms.TextInput(attrs={
        "class": "custom-class",
        "placeholder": "Title",
    }))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "my-custom-class",
            "placeoholder": "description",
            "some-attr": "This",
        }
    ))
    price = forms.DecimalField()
    publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISH_CHOICES, required=False)

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 1.00:
            raise forms.ValidationError("Price must be greater than 1")
        elif price >= 99.99:
            raise forms.ValidationError("Price must be less than 100")
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get("price")
        if len(title) > 3:
            return title
        else:
            raise forms.ValidationError("Title must be greater than 3 characters long")


class ProductModelForm(forms.ModelForm):
    tags = forms.CharField(label="Related tags", required=False)
    publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISH_CHOICES, required=False)

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
        ]
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "placeholder": "New Description"
                }
            ),
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Title"
                }
            )
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super(ProductModelForm, self).clean(*args, **kwargs)
        # title = cleaned_data.get('title')
        # slug = slugify(title)
        # qs = Product.objects.filter(slug=slug).exists()
        # if qs:
        #     raise forms.ValidationError('Title is taken, A new title is needed')

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 1.00:
            raise forms.ValidationError("Price must be greater than 1")
        elif price >= 100:
            raise forms.ValidationError("Price must be less than 100")
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > 3:
            return title
        else:
            raise forms.ValidationError("Title must be greater than 3 characters long")

