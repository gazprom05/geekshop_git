from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from authapp.models import ShopUser
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import ShopUserCreateForm,ShopUserUpdateForm
from django.urls import reverse


# Create your views here.
@user_passes_test
def main(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list
    }
    return render(request, 'adminapp/users.html', context)

def user_create(request):
    title = 'новый пользователь'

    if request.method == 'POST':
        form = ShopUserCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:main'))
    else:
        form = ShopUserCreateForm()

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/user_update.html', context)


def user_update(request, pk):
    title = 'редактирование пользователя'
    updated_user = get_object_or_404(ShopUser, pk=int(pk)

    if request.method == 'POST':
        form = ShopUserUpdateForm(request.POST, request.FILES, instance=updated_user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:main'))
    else:
        form = ShopUserUpdateForm(instance=updated_user)

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/user_update.html', context)