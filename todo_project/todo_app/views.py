from django.shortcuts import redirect, render

from django.views import View

from todo_app.forms import TaskForm

from todo_app.models import Task

# Create your views here.

class HomeView(View):
    '''
    HomeView functions as the site's homepage, listing out all the Task objects in the database and linking out to each one's detail view
    '''
    def get(self, request):
        '''The content required to render the homepage'''
        task_form = TaskForm()
        tasks = Task.objects.all()

        html_data = {
            'task_list': tasks,
            'form': task_form,
        }
        
        return render(
            request=request,
            template_name='index.html',
            context=html_data
        )

    def post(self, request):
        print(request.POST)
        task_form = TaskForm(request.POST)
        task_form.save()

        return redirect('home')


class TaskDetailView(View):
    def get(self, request, task_id):
        '''
        This is called a DocString...comments should be made in every method!
        '''
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(instance=task)        

        html_data = {
            'task_object': task,
            'form': task_form,
        }
        
        return render(
            request=request,
            template_name='detail.html',
            context=html_data
        )

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)

        if 'update' in request.POST:
            task_form = TaskForm(request.POST, instance=task)
            task_form.save()
        elif 'delete' in request.POST:
            task.delete()

        # print(request.POST)
        return redirect('home')


