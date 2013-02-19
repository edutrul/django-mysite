# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Poll, Choice
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

def index(request):
    latest_poll_list = Poll.objects.all().order_by('pub_date')[:5]
    #output = ', '.join([p.question for p in latest_poll_list])
    #~ t = loader.get_template('polls/index.html')
    #~ c = Context({
        #~ 'latest_poll_list': latest_poll_list,
    #~ })
    #~ return HttpResponse(t.render(c))
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    #~ try:
        #~ poll = Poll.objects.get(pk=poll_id)
    #~ except Poll.DoesNotExist:
        #~ raise Http404
    #~ return render_to_response('polls/detail.html', {'poll': poll})
    # shortcut for error 404
    poll = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': poll}, context_instance=RequestContext(request))

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': poll})

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.return
        return HttpResponseRedirect(reverse('polls.views.results', args=(poll.id,)))
    #return HttpResponse("You're voting on poll {poll_id}".format(poll_id=poll_id))