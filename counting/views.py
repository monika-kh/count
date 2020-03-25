import operator

from django.shortcuts import render


def home(request):
    return render(request, "homepage.html")


def count(request):
    words = request.GET.get("text")
    str = words.split()
    res = len(str)
    word_list = {}
    for word in str:
        if word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1
    sort = sorted(word_list.items(), key=operator.itemgetter(1))
    return render(request, "count.html", {"word": words, "res": res, "word_list": sort})
