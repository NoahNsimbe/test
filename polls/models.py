from django.db import models


def images_folder(instance, filename):
    folder = str(instance.firstName) + str(instance.lastName)
    return 'candidates/{0}/images/{1}'.format(folder, filename)


class Candidates(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    image = models.ImageField(upload_to=images_folder)
