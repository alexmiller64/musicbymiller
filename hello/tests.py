from django.test import TestCase
from hello.views import get_index
from django.core.urlresolvers import resolve


class HomePageTest(TestCase):

    def test_home_page_status_code_is_ok(self):
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)
