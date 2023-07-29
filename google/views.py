from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    return render(request, 'index.html')


def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        url = "https://google-web-search1.p.rapidapi.com/"
        querystring = {"query": f"{search}",
                       "limit": "20", "related_keywords": "true"}

        headers = {
            "X-RapidAPI-Key": "e1ade27b09msh8d03b634f457a5bp1a3d14jsn2140c4678005",
            "X-RapidAPI-Host": "google-web-search1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        knowledge_panel = response.json()['knowledge_panel']
        response_results = response.json()['results']
        # For Search Results
        final_result = []
        for i in range(len(response_results)):
            result_url = response_results[i]['url']
            result_title = response_results[i]['title']
            result_description = response_results[i]['description']
            final_result.append((result_url, result_title, result_description))
        context = {
            'final_result': final_result
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')
