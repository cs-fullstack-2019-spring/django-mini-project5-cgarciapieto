from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from .forms import RecipeModel, NewProfileModel, newProfileForm, RecipeForm

from django.contrib.auth.models import User

# this page renders from startup, if user is logged in, the user can see all entries
def index(request):
    if request.user.is_authenticated:

        profile = NewProfileModel.objects.get(name=request.user)

        allEntries = RecipeModel.objects.filter(foreignkeyToNewProfile=profile)
    else:
        allEntries = ""

    context = {'allEntries': allEntries}

    return render(request, 'recipeApp/index.html', context)

# this creates a user and saves it the database
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

# function that renders the form to add a recipe to a LOGGED IN user
def addRecipe(request):
    form = RecipeForm()
    context = {
        'recipeform': form
    }
    return render(request, 'recipeApp/addrecipe.html', context)

# renders the data/details of the page.
def recipeInfo(request):
    form = RecipeForm(request.POST)
    print(request.user)
    profile = NewProfileModel.objects.get(name=request.user)

    newform = form.save(commit=False)
    newform.foreignkeyToNewProfile = profile
    newform.save()
    return render(request, 'recipeApp/addrecipe.html',)


# renders a selected object and allows it to be changed/edited,

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

# deletes a recipe
def deleteRecipe(request, recipeID):
    deleteThisrecipe = get_object_or_404(RecipeModel, pk=recipeID)
    deleteThisrecipe.deltet()
    return redirect('index')
