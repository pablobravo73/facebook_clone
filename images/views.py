from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

@login_required # this decorator will make sure that only authenticated users can access this view
def image_create(request): # this view will be used to create new images
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.isvalid():
            # form data is valid 
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # assign current user to the item
            new_image.user = request.user # request.user is the currently logged in user
            new_image.save()
            messages.success(request,
                            'Image added successfully')
            # redirect to new created item detail view
            return redirect(new_image.get_absolute_url())
        else:
            # build form with data provided by the bookmarklet via GET
            form = ImageCreateForm(data=request.GET)
        return render(request,
                    'images/image/create.html',
                    {'section': 'images',
                    'form': form})





