from django.shortcuts import render
from .models import Contact
# from django.http import HttpResponse

def index(request):
    return render(request,"textmodifier/index.html")

def about(request):
    return render(request,"textmodifier/about.html")

def analyze(request):

    #Get the text
    giventext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    lowercase = request.GET.get('lowercase', 'off')
    uppertitle = request.GET.get('uppertitle', 'off')
    sentencecase = request.GET.get('sentencecase', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charactercount = request.GET.get('charactercount', 'off')
    numberremover = request.GET.get('numberremover', 'off')

    #Check which checkbox is on
    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        modified = ""
        for char in giventext:
            if char not in punctuations:
                modified = modified + char
        params = {'purpose': 'DOWN BELOW HERE IS YOUR MODIFIED TEXT', 'modified_text': modified}
        giventext = modified

    if(fullcaps=="on"):
        modified = ""
        for char in giventext:
            modified = modified + char.upper()

        params = {'purpose': 'DOWN BELOW HERE IS YOUR UPPER CASE TEXT', 'modified_text': modified}
        giventext = modified

    if (lowercase == "on"):
        modified = ""
        for char in giventext:
            modified = modified + (char.lower())

        params = {'purpose': 'DOWN BELOW HERE IS YOUR LOWER CASE TEXT', 'modified_text': modified}
        giventext = modified

    if (uppertitle == "on"):
        modified = ""
        modified = modified + giventext.title()

        params = {'purpose': 'DOWN BELOW HERE IS YOUR UPPERTITLE CASE TEXT', 'modified_text': modified}
        giventext = modified

    if (sentencecase == "on"):
        modified = ""
        modified = modified + ". ".join([word.capitalize() for word in giventext.split(". ")])

        params = {'purpose': 'DOWN BELOW HERE IS YOUR SENTENCE CASE TEXT', 'modified_text': modified}
        giventext = modified

    if (newlineremover == "on"):
        modified = ""
        for char in giventext:
            if char != "\n" and char != "\r":
                modified = modified + char
            else:
                print("no")
        print("pre", modified)
        params = {'purpose': 'DOWN BELOW HERE IS YOUR MODIFIED TEXT', 'modified_text': modified}
        giventext = modified

    if(extraspaceremover=="on"):
        modified = ""
        for index, char in enumerate(giventext):
            if not(giventext[index] == " " and giventext[index + 1] == " "):
                modified = modified + char

        params = {'purpose': 'DOWN BELOW HERE IS YOUR MODIFIED TEXT', 'modified_text': modified}
        giventext = modified

    if (numberremover == "on"):
        modified = ""
        numbers = '''0123456789'''

        for char in giventext:
            if char not in numbers:
                modified = modified + char

        params = {'purpose': 'DOWN BELOW HERE IS YOUR NUMBER LESS TEXT ', 'modified_text': modified}
        giventext = modified

    if(charactercount == "on"):
        modified = ""
        modified = len(giventext)

        params = {'purpose': 'Total Number of Character in Your given Text are', 'modified_text': modified}
        giventext = modified


    if (removepunc != "on" and fullcaps != "on" and  lowercase !="on" and uppertitle !="on" and
            newlineremover != "on" and extraspaceremover != "on" and numberremover != "on" and charactercount != "on" and sentencecase != "on"):
        # return HttpResponse("please select any operation and try again")
        return render(request, 'textmodifier/error.html')

    return render(request, "textmodifier/analyze.html", params)


def error(request):
    return render(request,"textmodifier/error.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        # print(name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'textmodifier/contact.html')




