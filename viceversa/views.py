from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['reverse']
    wordcountlist = []
    for i in user_text.split():
        wordcountlist.append(i.strip('!,. -_:;?'))
    wordcount = len(wordcountlist)
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text, 'wordcount': wordcount})