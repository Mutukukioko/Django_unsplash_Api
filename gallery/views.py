from django.shortcuts import render
import requests

def image_gallery(request):
    selected_category = request.GET.get('category', 'nature')  
    # Fetch images from Unsplash API
    # Replace 'YOUR_ACCESS_KEY' with your actual Unsplash API access key
    response = requests.get(f'https://api.unsplash.com/photos/?client_id=YOUR-ACCESSS-KEY&query={selected_category}')
    images = response.json()
    print(response.content)
    context = {'images': images}
    return render(request, 'gallery/image_gallery.html', context)
