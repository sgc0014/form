from django.shortcuts import render
from .modelform import NameForm
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'Post':
        form = NameForm(request.post)

        if form.is_valid():
            form.save()
        context = {
            'form': form
        }
        return render(request, 'index.html', {'form': form})
    else:
        form = NameForm()
        return render(request, 'index.html', {'form': form})


