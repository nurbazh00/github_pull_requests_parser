from django import forms
from django.core.exceptions import ValidationError

from .models import UserRequest


class IndexForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = ['url']

    def clean_url(self):
        new_url = self.cleaned_data['url']
        if new_url.startswith('https://github.com'):
            return new_url
        raise ValidationError('ссылка должна начинаться вот так "https://github.com/"')

















# class IndexForm(forms.ModelForm):
#     url = forms.RegexField(
#         regex=r'((git|ssh|http(s)?)|(git@[\w\.]+))(:(//)?)([\w\.@\:/\-~]+)(\.git)(/)?',
#         widget=forms.TextInput(attrs={
#             'placeholder': 'вставьте правильную ссылку для просмотра'}),
#         label=False, required=True, max_length=500)
#
#     class Meta:
#         model = UserRequest
#         fields = ['url']
















