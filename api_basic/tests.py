from django.test import TestCase
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class ArticleTestClass(TestCase):

    def setUp(self):
        self.a = Article(title="Article title",author="jaewon",email="rkdals3912@naver.com")
        self.b = Article(title="New title",author="jaewon",email="rkdals3912@naver.com")
        self.a.save()
        self.serializer = ArticleSerializer(self.a)

    def test_Instance(self):
        self.assertTrue(self.a)

    def test_Article_title(self):
        self.assertEqual("Article title",self.a.title)

    def test_articles(self):
        self.assertNotEqual(self.b.title,self.a.title)

    def test_author(self):
        self.assertEqual(self.a.author,self.b.author)
        # print(self.serializer.data)

    def test_serializer(self):
        self.content = JSONRenderer().render(self.serializer.data)
        print(self.content)


