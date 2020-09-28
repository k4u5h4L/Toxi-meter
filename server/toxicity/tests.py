from django.test import TestCase
from .models import Tox

# Create your tests here.


class ToxModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tox.objects.create(title='first Tox')
        Tox.objects.create(description='a description here')

    def test_title_content(self):
        Tox = Tox.objects.get(id=1)
        expected_object_name = f'{Tox.title}'
        self.assertEquals(expected_object_name, 'first Tox')

    def test_description_content(self):
        Tox = Tox.objects.get(id=2)
        expected_object_name = f'{Tox.description}'
        self.assertEquals(expected_object_name, 'a description here')
