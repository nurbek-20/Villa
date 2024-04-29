from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Villa, Storage
from .filters import VillaFilter
from .form import VillaUpdateForm


def index_view(request):
    villas = Villa.objects.filter(is_active=True)[:6]
    return render(request, 'app/index.html', {'villas': villas})


class VillaListView(ListView):
    model = Villa
    template_name = 'app/villa_list.html'
    context_object_name = 'villas'
    filterset_class = VillaFilter
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = VillaFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filter'] = self.filterset

        villas = context['villas']
        paginator = Paginator(villas, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            villas = paginator.page(page)
        except PageNotAnInteger:
            villas = paginator.page(1)
        except EmptyPage:
            villas = paginator.page(paginator.num_pages)
        context['villas'] = villas

        return context


def villa_detail_view(request, pk):
    villa = Villa.objects.filter(id=pk).first()

    if 'buy' in request.POST:
        storage = Storage(
            user=request.user,
            villa=villa
        )
        storage.save()
        return redirect('index')

    return render(request, 'app/villa_details.html', {'villa': villa})


@user_passes_test(lambda u: u.status == 2 or u.is_admin, login_url='/index/')
def villa_update_view(request, pk):
    villa = Villa.objects.filter(id=pk).first()

    if request.method == 'POST':
        form = VillaUpdateForm(request.POST, request.FILES, instance=villa)

        if form.is_valid():
            form.save()
            return redirect('villa_detail', villa.id)

    form = VillaUpdateForm(instance=villa)
    return render(request, 'app/villa_update.html', {'form': form})


def villa_delete_view(request, pk):
    villa = Villa.objects.filter(id=pk).first()
    villa.delete()
    return redirect('index')