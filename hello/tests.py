from django.test import TestCase
from blog.views import post_list
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from accounts.models import User


class HomePageTest(TestCase):

    # fixtures = ['subjects', 'user']

    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, post_list)

    def test_home_page_status_code_is_ok(self):
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)

    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "blogposts.html")
        home_page_template_output = render_to_response("blogposts.html").content
        self.assertEqual(home_page.content, home_page_template_output)

    def setUp(self):
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('letmein')
        self.user.save()

    def test_login(self):
        login = self.client.login(username='testuser', password='letmein')
        self.assertTrue(login)

    def test_home_page_uses_index_view(self):
        home_page = resolve('/blog/')
        self.assertEqual(home_page.func, post_list)

    def test_home_page_uses_index_template(self):
        home_page = self.client.get('/blog/')
        self.assertTemplateUsed(home_page, "blogposts.html")

    def test_home_page_logged_in_content(self):
        self.client.login(username='testuser', password='letmein')
        home_page = self.client.get('/blog/')

        home_page_template_output = render_to_response(
            "blogposts.html", {'user': self.user}).content
        self.assertEquals(home_page.content, home_page_template_output)
