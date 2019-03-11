from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from .forms import RecipeModel, NewProfileModel, newProfileForm, RecipeForm

from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:

        profile = NewProfileModel.objects.get(name=request.user)

        allEntries = RecipeModel.objects.filter(foreignkeyToNewProfile=profile)
    else:
        allEntries = ""

    context = {'allEntries': allEntries}

    return render(request, 'recipeApp/index.html', context)


def newUser(request):

        form = newProfileForm(request.POST or None)
        if form.is_valid():
            form.save()
            User.objects.create_user(request.POST['name'], '', request.POST['password1'])
            return redirect('index')
        else:

            context = {'errors': form.errors,
                   'form': form
                   }
        return render(request, 'recipeApp/newuser.html', context)


def addRecipe(request):
    form = RecipeForm()
    context = {
        'recipeform': form
    }
    return render(request, 'recipeApp/addrecipe.html', context)


def recipeInfo(request):
    form = RecipeForm(request.POST)
    print(request.user)
    profile = NewProfileModel.objects.get(name=request.user)

    newform = form.save(commit=False)
    newform.foreignkeyToNewProfile = profile
    newform.save()
    return render(request, 'recipeApp/addrecipe.html',)


    # if form.is_valid():
    #     form.save()
    #     RecipeModel.objects.create(name=request.POST['name'], imageURL=request.POST['imageURL'],
    #                                description=request.POST['description'], ingredients=request.POST['ingredients'],
    #                                dateCreated=request.POST['dateCreated'])
    #
    #
    #     return redirect('index')
    # else:
    #     context = {'recipeform:form,'
    #                'errors': form.errors}
    #     return render(request, 'recipeApp/addrecipe.html', context)


def editRecipe(request, recipeID):
    editthisrecipe = get_object_or_404(RecipeModel, pk=recipeID)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=editthisrecipe)
        if form.is_valid():
            form.save()
        else:
            print('not valid')
        return redirect('index')
    form = RecipeForm(instance=editthisrecipe)
    context = {
        'recipeform': form,
        'recipeID': recipeID
    }

    return render(request, 'recipeApp/editrecipe.html', context)


def deleteRecipe(request, recipeID):
    deleteThisrecipe = get_object_or_404(RecipeModel, pk=recipeID)
    deleteThisrecipe.deltet()
    return redirect('index')
