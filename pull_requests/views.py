import asyncio
from django.shortcuts import render
from .models import *
from .forms import IndexForm
from .services import get_pull_count, create_tasks, data


def get_index(request):
    return render(request, 'index.html')


def make_request(request):
    form = IndexForm(request.POST)
    try:
        url = request.POST.get("url", "")
        user_request = UserRequest.objects.get(url=url)
        pulls = UserRequestResult.objects.filter(url=user_request)
        return render(request, 'index.html', context={'pulls': pulls})

    except UserRequest.DoesNotExist:

        if form.is_valid():
            url = form.cleaned_data['url']
            count = get_pull_count(url)
            if count == 0:
                empty = 'pull requests нет'
                return render(request, 'index.html', context={'empty': empty})

            asyncio.run(create_tasks(url, count+1))

            try:
                return render(request, 'index.html', context={'empty': data[0]["message"]})
            except TypeError:
                    form.save()
                    user_request = UserRequest.objects.get(url=url)
                    for data_list in data:
                        for i in data_list:
                            user_request_result_model = UserRequestResult()
                            user_request_result_model.url = user_request
                            user_request_result_model.pull_name = i["title"]
                            user_request_result_model.reviewers_name = i["user"]["login"]
                            user_request_result_model.assignees_name = i["base"]["user"]["login"]
                            user_request_result_model.pull_url = i["html_url"]
                            user_request_result_model.save()
                            pulls = UserRequestResult.objects.filter(url__url=url)
            return render(request, 'index.html', context={'pulls': pulls})

        return render(request, 'index.html', context={'form': form})

    return render(request, 'index.html')