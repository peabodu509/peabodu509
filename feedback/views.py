from django.shortcuts import render, get_object_or_404, redirect
from .models import Feedback
from django.utils import timezone
from .forms import FeedbackForm

# Create your views here.
def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-created_date')
    count = feedbacks.count()
    for feedback in feedbacks:
        feedback.number = count
        count -= 1
        feedback.save()

    return render(request, 'feedback/feedback_list.html', {'feedbacks':feedbacks})

def feedback_detail(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    return render(request, 'feedback/feedback_detail.html', {'feedback': feedback})

def feedback_new(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
        return render(request, 'feedback/feedback_edit.html', {'form': form})