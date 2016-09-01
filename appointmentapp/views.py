from django.shortcuts import render
from .models import Appointments
from form import MyModelForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context_processors import csrf


from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
import json

# from .workday import *
# from .forms import *
import datetime
from .models import *
from django.template import RequestContext


@csrf_exempt
def ajax(request):
    args = {}
    args.update(csrf(request))

    if request.method == 'POST':
        form = MyModelForm(request.POST)
        print "post"
        print type(request.body)
        search = request.body.split("=")[1]
        # queryset = Appointments.objects.all()
        rec = Appointments.objects.filter(description__icontains=search)
        date, time, description = [], [], []
        l = len(rec)
        for i in rec:
            date.append(str(i.datetime).split()[0])
            time.append(str(i.datetime).split()[1].split("+")[0][:-3])
            description.append(str(i.description))
        print "doneeeeeeeeeeeee"
        print(zip(date,time,description))
        return HttpResponse(json.dumps({'d': date, 't': time, 'des': description}), content_type="application/json")
        # return render(request, json.dumps(zipped), {'form': form, 'records': zipped, 'length': l})
    return render_to_response("new/appointmentpage.html", args)



@csrf_exempt
def home_page(request):
    args = {}
    args.update(csrf(request))

    print "view vapus chala"
    if request.method == 'POST':
       form = MyModelForm(request.POST)
       # form = Appointments.objects.create()
       print "insideeeeeeeeeeee"
       print(request.POST, "===========>", form)
       if form.is_valid():
           print("------- valid")
           form.datetime = request.POST.get('datetime')
           form.description = request.POST.get('description')
           print request.POST.get('datetime')
           form.save()
       else:
           print(form.errors, "---------->")

       # print form['datetime']
       # print form['description']
       # print"post chala"
       # # form = MyModelForm(request.POST)
       # if form.is_valid():
       #     data = form.save(commit=False)
       #     data.save()
       #     #return HttpResponseRedirect('/myidea/')
       my_appointments = Appointments.objects.all()
       my_articles = Appointments.objects.all()
       l = len(my_articles)
       date, time, description = [], [], []
       for i in my_articles:
           date.append(str(i.datetime).split()[0])
           time.append(str(i.datetime).split()[1].split("+")[0][:-3])
           description.append(str(i.description))
       zipped = zip(date, time, description)
       return render_to_response('new/appointmentpage.html', {'form': form, 'records': zipped, 'length': l,'my_data': form, 'my_appointments':my_appointments})


    else:
        print "elseeeeeeeeeeeeee"
        form = MyModelForm()
       #return render(request, 'hello.html', {'form': form})
       # return render_to_response('new/hello.html', {'my_data': form})
        my_articles = Appointments.objects.all()
        l = len(my_articles)
        date, time, description = [], [], []
        for i in my_articles:
            date.append(str(i.datetime).split()[0])
            time.append(str(i.datetime).split()[1].split("+")[0][:-3])
            description.append(str(i.description))
        zipped = zip(date, time, description)
        return render(request, 'new/appointmentpage.html', {'form': form, 'records': zipped, 'length': l})

        # return render_to_response('new/appointmentpage.html', {'my_appointments':my_appointments})




       #
   # my_data = "manishaaaaaa"
   # return render_to_response('new/hello.html', { 'my_data': my_data})
   # else:
   #     user_loggedin = str(request.user)
   #     my_data = Note.objects.all().filter(logged_user=user_loggedin)
   #     return render_to_response('notes.html', {'user_loggedin': user_loggedin, 'my_data': my_data},
   #                               context_instance=RequestContext(request))


