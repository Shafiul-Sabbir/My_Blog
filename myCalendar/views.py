from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from calendar import HTMLCalendar
from datetime import datetime
from calendar import monthcalendar
# Create your views here.
def generate_calendar_data(year, month):
    # Get the calendar data for the given year and month
    cal_data = monthcalendar(year, month)
    # Initialize an empty list to store calendar data
    calendar_data = []
    # using id for each day
    id = 0
    # Iterate over each week in the calendar data
    for week in cal_data:
        week_data = []
        # Iterate over each day in the week
        for day in week:
            if(day != 0):
                id = id + 1
                
            day_data = {
                'day': day,
                'day_id' : id,
            }
            week_data.append(day_data)
        calendar_data.append(week_data)
    return calendar_data

now = datetime.now()
current_year = now.year
current_month = now.month

def home(request, year=None, month=None):
    if year is None or month is None:
        # If year or month is not provided in the URL parameters, use the current year and month
        now = datetime.now()
        if year is None:
            year = now.year
        if month is None:
            month = now.month
    else:
        # Convert year and month from string to integer
        year = int(year)
        month = int(month)
        
    current_date = now.day
    date_format = "%A - %d %B, %Y :: %I : %M ( %p )"
    formatted_date = now.strftime(date_format)
    month_year = now.strftime("%B, %Y")
    
    # cal = HTMLCalendar().formatmonth(current_year, current_month)
    calendar_data = generate_calendar_data(current_year, current_month)

    context={
        'calendar_data': calendar_data,
        'year' : current_year,
        'month' : current_month,
        'date' : current_date,
        'formatted_date' : formatted_date,
        'month_year' : month_year,
        'title' : 'My Calendar',
    }
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # If it's an AJAX request, return the updated calendar data as JSON response
        return JsonResponse(calendar_data)
    
    # If it's a regular request (not AJAX), render the template as before
    return render(request, 'myCalendar/calendar.html', context)

def update_calendar(request, year=None, month=None):
    if year is None or month is None:
        # If year or month is not provided in the URL parameters, use the current year and month
        now = timezone.now()
        if year is None:
            year = now.year
        if month is None:
            month = now.month
    else:
        # Convert year and month from string to integer
        year = int(year)
        month = int(month)
        
    calendar_data = generate_calendar_data(year, month)
    
    # Return the updated calendar data as JSON response
    return JsonResponse(calendar_data)
