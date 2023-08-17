from django.shortcuts import render
import requests

def image_gallery(request):
    # Fetch images from Unsplash API
    # Replace 'YOUR_ACCESS_KEY' with your actual Unsplash API access key
    response = requests.get('https://api.unsplash.com/photos/?client_id=OeBTDjutwsJi5BC0gy1UAfl4i4lhLHYuqDJgvbcdciM&query={selected_category}')
    images = response.json()

    context = {'images': images}
    return render(request, 'gallery/image_gallery.html', context)
