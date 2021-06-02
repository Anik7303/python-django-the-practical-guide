from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Eat no meat for the entire month!',
    'may': 'Walk for at least 20 minutes every day!',
    'june': 'Learn Django for at least 20 minutes every day!',
    'july': 'Eat no meat for the entire month!',
    'august': 'Walk for at least 20 minutes every day!',
    'september': 'Learn Django for at least 20 minutes every day!',
    'october': 'Eat no meat for the entire month!',
    'november': 'Walk for at least 20 minutes every day!',
    'december': 'Learn Django for at least 20 minutes every day!',
}


def index(request):
    list_items = ''

    months = list(monthly_challenges.keys())
    for month in months:
        month_name = month.capitalize()
        url = reverse('monthly_challenges', args=[month])
        list_items += f'<li><a href=\"{url}\">{month_name}</a></li>'

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):

    months = list(monthly_challenges.keys())

    if month > len(monthly_challenges):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    redirect_url = reverse('monthly_challenges', args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported!')
