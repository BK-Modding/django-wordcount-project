from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_occ = count_the_words(fulltext)
    print(word_occ)
    max = sorted(word_occ, key=word_occ.get, reverse=True)[0]
    return render(request, 'count.html', {"occurances": word_occ, "total_len": len(fulltext.split(' ')), "fulltext": fulltext, "max_occur": max, "max_occur_times": word_occ[max]})

def about(request):
    return render(request, 'about.html')


def count_the_words(text):
    word_arr = text.split(' ')
    checked_arr = []
    count_dict = {}
    for word in word_arr:
        if word not in checked_arr:
            count_dict[word] = word_arr.count(word)
            checked_arr.append(word)

    return count_dict
