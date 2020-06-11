from django.shortcuts import render
from .models import Poll, Option
from django.views.generic import ListView,DetailView,RedirectView, CreateView, UpdateView, DeleteView

# Create your views here.
def poll_list(req):
    polls = poll.objects.all()
    return render(req,'poll_list.html',{'poll_list':polls})
class PollList(ListView):
    model = Poll

class PollView(DetailView):
    model = Poll

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['option_list'] = Option.objects.filter(poll_id=self.kwargs['pk'])
        return data
class PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        opt = Option.objects.get(id=self.kwargs['oid'])
        opt.count += 1
        opt.save()
        return'/poll/{}/'.format(opt.poll_id)
class Pollcreate(CreateView):
    model = Poll
    fields = ['title', 'desc']
    success_url = '/poll/'

class PollEdit(UpdateView):
    model = Poll
    fields = ['title','desc']
    success_url = '/poll/'

class Optioncreate(CreateView):
    model = Option
    fields = ['title', 'count']
    success_url = '/poll/'

    def get_success_url(self):
        return '/poll/{}/'.format(self.kwargs['pid'])

        def form_valid(self, form):
            form.instance.poll.id = self.kwargs['pid']
            return super().form_valid(form)

class OptionEdit(UpdateView):
    model = Option
    fields = ['title', 'count']            

    def get_success_url(self):
        return '/poll/{}/'.format(self.object.poll_id)
        
class OptionDelete(DeleteView):
    model = Option
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return 'poll/{}/'.format(self.object.poll_id)
          

class PollDelete(DeleteView):
    model = Poll
    success_url = '/poll/'
    template_name = 'confirm_delete.html'