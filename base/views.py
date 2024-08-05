# offerletter/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Candidate, OfferLetter
from .forms import CandidateForm, OfferLetterForm
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
import pdfkit

@login_required
def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:candidate_list')
    else:
        form = CandidateForm()
    return render(request, 'add_candidate.html', {'form': form})

@login_required
def update_candidate(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        form = CandidateForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('base:candidate_list')
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'update_candidate.html', {'form': form})

@login_required
def delete_candidate(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        candidate.delete()
        return redirect('base:candidate_list')
    return render(request, 'delete_candidate.html', {'candidate': candidate})

@login_required
def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidates})

@login_required
def create_offer_letter(request):
    if request.method == 'POST':
        form = OfferLetterForm(request.POST)
        if form.is_valid():
            offer_letter = form.save(commit=False)
            offer_letter.created_by = request.user
            offer_letter.save()
            return redirect('base:offer_letter_list')
    else:
        form = OfferLetterForm()
    return render(request, 'create_offer_letter.html', {'form': form})

@login_required
def offer_letter_list(request):
    offer_letters = OfferLetter.objects.all()
    return render(request, 'offer_letter_list.html', {'offer_letters': offer_letters})

@login_required
def view_offer_letter(request, pk):
    offer_letter = get_object_or_404(OfferLetter, pk=pk)
    return render(request, 'view_offer_letter.html', {'offer_letter': offer_letter})
@login_required
def download_offer_letter(request, pk):
    offer_letter = get_object_or_404(OfferLetter, pk=pk)
    html = render_to_string('offer_letter_pdf.html', {'offer_letter': offer_letter})

    # Configure pdfkit with the wkhtmltopdf path
    config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_CMD)
    pdf = pdfkit.from_string(html, False, configuration=config)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="offer_letter_{pk}.pdf"'
    return response


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("base:home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def login(request):
    return render(request, 'home.html')
