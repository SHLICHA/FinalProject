from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .forms import ObjectForm
from .functions import MNSSD_process_image
from .models import Object


def paginator(request, posts, count):
    pag_temp = Paginator(posts, count)
    page_number = request.GET.get('page')
    return pag_temp.get_page(page_number)


class IndexView(TemplateView):
    template_name = 'object_detection/index.html'


def get_dashboard(request):
    if request.user.is_authenticated:
        objects_list = Object.objects.filter(user=request.user)
        page_obj = paginator(request, objects_list, 5)
        context = {
            'page_obj': page_obj,
        }
        return render(request, 'object_detection/dashboard.html', context)
    else:
        return redirect('login')


@login_required()
def add_object(request):
    if request.method == "POST":
        form = ObjectForm(request.POST, request.FILES)
        if form.is_valid():
            image_object = form.save(commit=False)
            image_object.user = request.user
            image_object.save()
            return redirect('dashboard')
    form = ObjectForm()
    return render(request, 'object_detection/add_image_feed.html', {'form': form})


@login_required()
def process_image_feed(request, image_id):
    """Можно расширить, добавив обработку другими моделями. Модель выбирает из предпочтений пользователя"""
    image = get_object_or_404(Object, id=image_id, user=request.user)
    model = image.model
    print(model)
    if model == 'MobileNet_SSD' or model == None:
        MNSSD_process_image(image_id)
    return redirect('dashboard')


@login_required()
def delete(request, image_id):
    Object.objects.get(
        id=image_id,
        user=request.user
    ).delete()
    return redirect('dashboard')

