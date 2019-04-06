from django.shortcuts import render
from .models import Record

def home(request):

    return render(request, 'wordcount/home.html')

def about(request):

    return render(request, 'wordcount/about.html')

def count(request):

    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}
    word_specific = ''
    
    str_dict_list = []

    for word in word_list:

        if word in word_dictionary:
            word_dictionary[word] +=1

        else:
            word_dictionary[word] =1

    for key, value in word_dictionary.items():
      str_dict_list.append(str(key) + ' - ' + str(value) + '(개) / ')

    for my_list in str_dict_list:
        word_specific += my_list

    Record(text=str(full_text), word_all_count = str(len(word_list)), word_count = word_specific).save()

    return render(request, 'wordcount/count.html', {'fulltext' : full_text, 'total' : len(word_list),
    'dictionary' : word_dictionary.items()})

def record(request):

    Records = Record.objects.all().order_by('-created_at')

    return render(request, 'wordcount/record.html', {'records' : Records})