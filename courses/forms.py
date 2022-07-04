from django import forms
from django.contrib.auth.models import User

from .models import Klasa, Lendet, Lesson



class KlasaForm(forms.ModelForm):
    class Meta:
        model = Klasa
        fields = '__all__'
        help_texts = {
            'Курстун_аты': 'Мис. 1-Курс',
            'Ачыктоо':'Курс тууралуу кыскача маалымат бериңиз',
            'Сурот':'Сиз курстун сүрөтүн коюуга болот же бош калтырылышы мүмкүн'
        }

class LendaForm(forms.ModelForm):
    class Meta:
        model = Lendet
        fields = ['krijues','slug', 'Курстун_аты', 'Класс', 'Ачыктоо', 'Сурот_туру']
        help_texts = {
            'Курстун_аты': 'Мис. Матемаматика',
            'Ачыктоо':'Сабак тууралуу кыскача Ачыктама',
            'Класс':'Курсуңузду тандаңыз',
            'Сурот_lendes':'Сиз курстун сүрөтүн коюуга болот же бош калтырылышы мүмкүн'
        }
        labels = {
            'Курстун_аты':'Мис. Тандаган курсуңуздун сабагын'
        }
        widgets = {'krijues': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class MesimiForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = '__all__'
        help_texts = {
            'Курстун_аты':'Тема же болбосо подтема',
            'Туру':'Тандалган Курстардын бирөөсүн тандаңыз',
            'Видео':'Сабактын видеосун бул жакка жүктөңүз',
            'Материалы':'Сабактын материалын бул жакка жүктөңүз',
            'Катары':'Vendosni numrin e Катарыt ose radhen e mesimit '
        }
        
       
        widgets = {
            'slug': forms.HiddenInput()
        }