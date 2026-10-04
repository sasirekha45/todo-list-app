from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todos = Todo.objects.all()

    # Search
    search_query = request.GET.get('q', '').strip()
    if search_query:
        todos = todos.filter(title__icontains=search_query) | todos.filter(description__icontains=search_query)

    # Filter by status
    status_filter = request.GET.get('status', 'all')
    if status_filter == 'completed':
        todos = todos.filter(completed=True)
    elif status_filter == 'pending':
        todos = todos.filter(completed=False)

    # Filter by priority
    priority_filter = request.GET.get('priority', 'all')
    if priority_filter in ['low', 'medium', 'high']:
        todos = todos.filter(priority=priority_filter)

    # Filter by category
    category_filter = request.GET.get('category', 'all')
    if category_filter and category_filter != 'all':
        todos = todos.filter(category=category_filter)

    # Quick inline create via POST
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm()

    all_todos = Todo.objects.all()
    today = timezone.now().date()
    stats = {
        'total': all_todos.count(),
        'completed': all_todos.filter(completed=True).count(),
        'pending': all_todos.filter(completed=False).count(),
        'overdue': all_todos.filter(completed=False, due_date__lt=today).count(),
    }

    categories = [cat[0] for cat in Todo.CATEGORY_CHOICES]

    context = {
        'todos': todos,
        'form': form,
        'stats': stats,
        'search_query': search_query,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'category_filter': category_filter,
        'categories': categories,
        'today': today,
    }
    return render(request, 'todos/todo_list.html', context)


def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'ok', 'completed': todo.completed})

    status_str = "completed" if todo.completed else "marked as pending"
    messages.info(request, f'Task "{todo.title}" {status_str}.')
    return redirect('todo_list')


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todos/todo_edit.html', {'form': form, 'todo': todo})


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    title = todo.title
    todo.delete()
    messages.warning(request, f'Task "{title}" has been deleted.')
    return redirect('todo_list')


def todo_clear_completed(request):
    if request.method == 'POST':
        deleted_count, _ = Todo.objects.filter(completed=True).delete()
        if deleted_count > 0:
            messages.success(request, f'Cleared {deleted_count} completed task(s)!')
        else:
            messages.info(request, 'No completed tasks to clear.')
    return redirect('todo_list')
