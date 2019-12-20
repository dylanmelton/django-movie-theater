from django.shortcuts import render
from app.models import Movie
from app.forms import NewTicketForm


# Create your views here.
def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})


def new_ticket(request, id):
    if request.method == "GET":
        movie = Movie.objects.get(id=id)
        return render(request, "new_ticket.html", {"movie":movie})
    if request.method == "POST":
        form = NewTicketForm(request.POST)
        if form.is_valid():
            the_new_ticket = Ticket.objects.create(id=showing_id)
            validated_id = form.cleaned_data['showing_id']
            validated_name = form.cleaned_data['name']
            
            
            return redirect("ticket_detail.html")
        else:
            return render(request, "new_ticket.html", {"movie":movie}) 


def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, "ticket_detail.html", {"ticket": ticket})

