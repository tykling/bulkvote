from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import CreateVoteForm, ChoiceForm
from .models import Vote, Item, Choice, UserChoice


def frontpage(request):
    form = CreateVoteForm(request.POST or None)
    if form.is_valid():
        ### create vote
        vote = Vote.objects.create(description=form.cleaned_data['description'], author=form.cleaned_data['author'])

        ### create items
        for item in form.cleaned_data['items'].split('\n'):
            if item != '':
                Item.objects.create(vote=vote, item=item.strip())

        ### create choices
        for choice in form.cleaned_data['choices'].split('\n'):
            if choice != '':
                Choice.objects.create(vote=vote, choice=choice.strip())

        return HttpResponseRedirect(reverse('showvote', kwargs={'uuid': str(vote.uuid)}))

    return render(request, 'frontpage.html', {
        'form': form,
    })


def showvote(request, uuid):
    vote = get_object_or_404(Vote, uuid=uuid)

    return render(request, 'showvote.html', {
        'vote': vote,
    })


def vote(request, uuid):
    vote = get_object_or_404(Vote, uuid=uuid)
    form = ChoiceForm(request.POST or None, vote=vote)
    if form.is_valid():
        for item in vote.items.all():
            UserChoice.objects.create(choice=form.cleaned_data['choice_for_item_%s' % item.id], item=item)
        return HttpResponseRedirect(reverse('showvote', kwargs={'uuid': str(vote.uuid)}))

    return render(request, 'vote.html', {
        'form': form,
    })

def vote_results(request, uuid):
    vote = get_object_or_404(Vote, uuid=uuid)

    return render(request, 'results.html', {
        'vote': vote,
    })

