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
        
class TestNumberOfFollowers(TestCase):

        
    def setUp(self):
        self.main_user = User(username="MaxMustermann");
        self.followed_user = User(username="HansHolbein");
        self.followed_user.save();
        
        self.following_user = User(username="RubenRembrandt");
        self.following_user.save();
        
        self.main_user = User(username="MaxMustermann");
        self.main_user.save();
        
        self.main_user.addFollower(self.followed_user);
        
        self.main_user.save();

        
    def testFollows(self):
        """ Test if user follows the right person! """
        
        self.main_user.addFollower(self.followed_user);
        print(self.followed_user.followers.all())
        self.assertEqual(self.main_user.follows.all()[0], self.followed_user);
        self.assertIn(self.main_user, self.followed_user.followers.all());
        
        
    def tearDown(self):
        self.followed_user.delete();
        self.following_user.delete();
        self.main_user.delete();
       
        
        