from .models import Task
from django.shortcuts import render
from .forms import TaskForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

class HomeView(ListView):
    queryset = Task.objects.order_by('-id')
    context_object_name = 'tasks'
    template_name = 'main/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main Page'
        return context

class TasksCreateView(CreateView):
    model = Task
    template_name = 'main/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать заметку'
        context['button'] = 'Add'
        return context

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'main/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать заметку'
        context['button'] = 'Update'
        return context

class TaskDeleteView(DeleteView,):
    model = Task
    success_url = reverse_lazy('home')
    success_msg = 'Запись удалена'
    def post(self, request, *args, **kwargs):
        context = super().post(request)
        messages.success(self.request, self.success_msg, )
        return context

def about(request):
    return render(request, 'main/about.html')






# def index(request):
#     tasks = Task.objects.order_by("-id")
#     content = {
#         'title': 'Main page',
#         'tasks': tasks
#     }
#     return render(request, 'main/index.html', content)



# def create(request):
#     error = 'Failed'
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             error
#     form = TaskForm()
#     content = {
#         'form': form,
#         'title': "Создать заметку",
#         'button': "Add"
#     }
#     return render(request, 'main/create.html', content)

# def update(request,id):
#     get_article =Task.objects.get(id=id)
#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=get_article)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = TaskForm(instance=get_article)
#         content = {
#         'form': form,
#         'title': "Редактирование",
#         'button': 'Update'
#                 }
#     return render(request, 'main/create.html', content)

# def delete(request,id):
#     get_article = Task.objects.get(id=id)
#     get_article.delete()
#     return redirect('home')





