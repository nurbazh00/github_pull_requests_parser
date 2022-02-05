from django.db import models


class UserRequest(models.Model):
    url = models.URLField(max_length=255)

    def __str__(self):
        return '{}'.format(self.url)


class UserRequestResult(models.Model):
    url = models.ForeignKey(UserRequest, on_delete=models.CASCADE)
    pull_name = models.CharField(max_length=255)
    reviewers_name = models.CharField(max_length=255)
    assignees_name = models.CharField(max_length=255)
    pull_url = models.URLField(max_length=255)
