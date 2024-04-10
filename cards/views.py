# cards/views.py

import random
from django.shortcuts import render  # Add this import
from .models import Flashcard
from .models import Card

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)

def welcome_page_view(request):
    # Logic to process the request (if needed)
    # Render the welcome page template
    return render(request, 'cards/welcome.html')  # Replace 'your_app/welcome.html' with the correct path to your welcome template

def existing_cards_view(request):
    card_data = [
        {'title': 'Card 1', 'front_content': 'Quand s\'arrête la boucle définie par cette instruction? while a<=6',
         'back_content': 'Quand >6'},
        {'title': 'Card 2', 'front_content': 'Front content for card 2', 'back_content': 'Back content for card 2'},
        {
            'title': 'Card 3',
            'front_content': 'What is the output of the following code?<br/><pre><code>for i in range(5):<br/>&nbsp;&nbsp;&nbsp;&nbsp;print(i)</code></pre>',
            'back_content': '0<br/>1<br/>2<br/>3<br/>4'
        }
    ]
    audio_file_path = '/static/page-turn.wav'  # Replace this with the actual path to your audio file
    return render(request, 'cards/existing_cards.html', {'card_data': card_data, 'audio_file_path': audio_file_path})

def create_cards_view(request):
    # Logic to process the request (if needed)
    # Render the welcome page template
    return render(request, 'cards/base.html')  # Replace 'your_app/welcome.html' with the correct path to your welcome template

