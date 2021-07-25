from django.test import TestCase, Client;
from .models import User, Post;
import unittest;


class Tests(TestCase):
    def setUp(self):
        self.client = Client();


    def test_get_login(self):
        """Test of client (login-page)"""
        response = self.client.get("/login");
        self.assertEqual(response.status_code, 200);
		
class TestUserCase(TestCase):
    def setUp(self):
        self.user = User(username="MaxMustermann");

    def testUser(self):
        """ Tests if username is just"""
        self.assertEqual(self.user.username, "MaxMustermann");
        self.assertEqual(self.user.__str__(), "MaxMustermann");
        
class TestPostCase(TestCase):
    def setUp(self):
        self.post = Post(content = "Test test", author = User(username="Incognito"));
        
    def testPost(self):
        """Test if post is properly set up"""
        self.assertEqual(self.post.author.username, "Incognito");
        self.assertEqual(self.post.content, "Test test");