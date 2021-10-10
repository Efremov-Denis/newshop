from django.shortcuts import render

def main(request):
    context = {
        'first_line': 'Информация, отображаемая на главной странице',
        'second_word': 'второе слово',
    }
    return render(request, 'mainapp/index.html', context)
    

def products(request):
    return render(request, 'mainapp/products.html')
    

def contacts(request):
    return render(request, 'mainapp/contacts.html')