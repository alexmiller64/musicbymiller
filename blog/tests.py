from django.test import TestCase
from .models import Post
from django.shortcuts import render_to_response


class PostTests(TestCase):

    def test_str(self):
        test_title = Post(title='My Latest Blog Post')
        self.assertEqual(str(test_title),
                         'My Latest Blog Post')


class SubjectPageTest(TestCase):
    def test_check_content_is_correct(self):
        subject_page = self.client.get('/blog/')
        self.assertTemplateUsed(subject_page, "blogposts.html")
        subject_page_template_output = render_to_response("blogposts.html",
                                                          {'posts':
                                                               Post.objects.all()}).content
        self.assertEqual(subject_page.content, subject_page_template_output)


