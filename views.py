from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Challenge

@login_required
def challenge_list(request):
    challenges = Challenge.objects.filter(assigned_to=request.user)
    return render(request, 'challenges/challenge_list.html', {'challenges': challenges})

@login_required
def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk, assigned_to=request.user)
    return render(request, 'challenges/challenge_detail.html', {'challenge': challenge})

@login_required
def mark_completed(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk, assigned_to=request.user)
    challenge.completed = True
    challenge.save()
    return redirect('challenges:list')
