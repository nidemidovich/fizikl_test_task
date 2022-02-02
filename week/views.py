import datetime
from django.http import HttpResponseBadRequest

from django.shortcuts import redirect, render

from .forms import DateForm
from .utils import count_weeks


def index(request):
    start_date = datetime.date(2019, 1, 1)
    weeks = 0

    if request.method == 'POST':
        form = DateForm(request.POST)

        if form.is_valid():
            given_date = form.cleaned_data['date']
            
            try:
                weeks = count_weeks(start_date, given_date)
            except:
                error = '<h1>Error 400, Bad Request</h1><h2>Start date is greater than end date</h2>'
                return HttpResponseBadRequest(error)

            request.session['weeks'] = weeks
            return redirect('weeks')
    else:
        form = DateForm()
    
    return render(request, 'week/index.html', context={'form': form})


def weeks(request):
    weeks = request.session.get('weeks')
    return render(request, 'week/weeks.html', context={'weeks': weeks})