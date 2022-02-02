import datetime

from django.urls import reverse
from django.test import Client
from django.test import TestCase


class CountWeeksTestCase(TestCase):

    def test_count_start_date_greater(self):
        client = Client()
        end_date = datetime.date(2000, 1, 1)
        response = client.post(reverse('index'), data={'date': end_date})
        self.assertEqual(response.status_code, 400)

    def test_count_end_date_greater(self):
        client = Client()
        end_date = datetime.date(2019, 1, 6)
        response = client.post(reverse('index'), data={'date': end_date})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(client.session['weeks'], 2)

    def test_count_end_date_equal(self):
        client = Client()
        end_date = datetime.date(2019, 1, 1)
        response = client.post(reverse('index'), data={'date': end_date})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(client.session['weeks'], 1)
