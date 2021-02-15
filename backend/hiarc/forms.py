from allauth.account.forms import SignupForm
from django import forms
from .models import *

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(required=True, label="이름", widget=forms.TextInput(attrs={'placeholder': '홍길동'}))
        self.fields['student_id'] = forms.CharField(required=True, label="학번", widget=forms.TextInput(attrs={'placeholder': 'C000000'}))
        self.fields['phone'] = forms.CharField(required=True, label="전화번호", widget=forms.TextInput(attrs={'placeholder': '01012345678'}))
        self.fields['major'] = forms.CharField(required=True, label="소속학과(주전공)", widget=forms.TextInput(attrs={'placeholder': '컴퓨터공학과'}))
        self.fields['attending_status'] = forms.ChoiceField(required=True, label="재학 학기(휴학생일 경우 수료 학기)", choices=(('재학 중', '재학 중'),('군휴학', '군휴학'),('일반휴학', '일반휴학')))
        self.fields['semester'] = forms.CharField(required=True, label="재학 학기(휴학생일 경우 수료 학기)", widget=forms.TextInput(attrs={'placeholder': '2-1'}))
        self.fields['boj_id'] = forms.CharField(required=True, label="BOJ ID", widget=forms.TextInput(attrs={'placeholder': '백준 아이디(핸들)'}))
        self.fields['codeforces_id'] = forms.CharField(required=False, label="Codeforces ID", widget=forms.TextInput(attrs={'placeholder': '코드포스 아이디(핸들)'}))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.student_id = self.cleaned_data['student_id']
        user.phone = self.cleaned_data['phone']
        user.major = self.cleaned_data['major']
        user.semester = self.cleaned_data['semester']
        user.attending_status = self.cleaned_data['attending_status']
        user.boj_id = self.cleaned_data['boj_id']
        user.codeforces_id = self.cleaned_data['codeforces_id']
        user.save()
        return user
