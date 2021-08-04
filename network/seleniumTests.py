from django.test import LiveServerTestCase;
from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.common.exceptions import NoSuchElementException;
from selenium.webdriver.common.action_chains import ActionChains;
import time;


# cd OneDrive\Desktop\LifeLongLearning\EdX\cs50_WebProgramming\CICD_Testing\network\project4

class MySeleniumTests(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Firefox();
        self.driver.get("http://127.0.0.1:8000/");
        
    def login(self):
        login_button = self.driver.find_element(By.ID, "log_in");
        login_button.click();
        
        username = self.driver.find_element(By.NAME, "username");
        username.send_keys("pflege");
        
        password = self.driver.find_element(By.NAME, "password");
        password.send_keys("511kefka!511");
        
        login_button = self.driver.find_element(By.CLASS_NAME, "btn.btn-primary");
        login_button.click();
        
    def go_to_all_posts(self):
        
        all_posts_nav = self.driver.find_element(By.ID, "all_posts");
        all_posts_nav.click();  
        time.sleep(2);
        
    def go_to_following(self):  
        following_nav = self.driver.find_element(By.ID, "following");
        following_nav.click();  
        time.sleep(2);
        
    def test_title(self):
        """test title """
        
        assert "Social" in self.driver.title;
        
    def test_navigation_menu(self):
        """test if items in navigation menu in order """
       
        all_nav_bar_names = [];          
        
        all_posts = self.driver.find_elements(By.TAG_NAME, "li");
        
        for listitem in all_posts:
            all_nav_bar_names.append(listitem.text);
                   
        assert "All Posts" in all_nav_bar_names;
        
    def test_login(self):
        """test if login works """
        self.login();
        
        all_nav_bar_names = []; 
        all_posts = self.driver.find_elements(By.TAG_NAME, "li");

        
        for listitem in all_posts:
            all_nav_bar_names.append(listitem.text);
                   
        assert "New Post" in all_nav_bar_names;
        
    def test_send(self):
        """test if I can create a new post """
        self.login();
        
        post_button = self.driver.find_element(By.ID, "new_post");
        post_button.click();
        
        textarea = self.driver.find_element(By.TAG_NAME, "textarea");
        textarea.send_keys("Test with Selenium");
        
        send_button = self.driver.find_element(By.CLASS_NAME, "btn.btn-primary");
        send_button.click();
        
        test_p = self.driver.find_element(By.ID, "dummy");       
        
        self.assertEqual(test_p.text, "Test with Selenium");
    
    def test_all_posts(self):
        """test if going to 'all posts' works!"""
        self.login();
        
        all_posts_nav = self.driver.find_element(By.ID, "all_posts");
        all_posts_nav.click();
        
        post_div = self.driver.find_element(By.ID, "compose-posts");
        
        self.assertEqual(post_div.text, "Posts to show");
        
    def test_posts_json(self):  
        """test if scrolling works """
        
        self.login();
        
        all_posts_nav = self.driver.find_element(By.ID, "all_posts");
        all_posts_nav.click();
        
        time.sleep(3);
       
        fifth_element = self.driver.find_element(By.ID, "5");
       
        #actions = ActionChains(self.driver);
        #actions.move_to_element(fifth_element).perform();
        
        self.driver.execute_script("arguments[0].scrollIntoView();", fifth_element);
        
        time.sleep(3);
        
        post_elements = self.driver.find_elements(By.CLASS_NAME, "posts");
        
        self.assertEqual(len(post_elements),10);
        
    def test_select_user_and_go_to_profile(self):
        """test if selecting a user works """
        self.login();        
        self.go_to_all_posts();
        
        link_to_user = self.driver.find_element_by_link_text("Hans");
        link_to_user.click();
        print("link is:" + str(link_to_user));
        
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "Hans");
        
    def test_cannot_follow_myself(self):
        """test to make sure that a user can't follow himself/herself"""
        self.login();        
        self.go_to_all_posts();
        
        link_to_user = self.driver.find_element_by_link_text("pflege");
        link_to_user.click();
        
        try:
            follow_button = self.driver.find_element(By.ID, "follow-btn");
        except NoSuchElementException:
            follow_button = None;
        finally:
            self.assertIsNotNone(follow_button);
    
    def test_unfollow(self):
        """test to make I can unfollow a followed user"""
        self.login();        
        self.go_to_all_posts();
        
        link_to_user = self.driver.find_element_by_link_text("Gretel");
        link_to_user.click();
        
        try:
            follow_button = self.driver.find_element(By.ID, "unfollow-btn");
        except NoSuchElementException:
            follow_button = None;
        finally:
            self.assertIsNotNone(follow_button);
            
    def test_is_follow_myself_disabled(self):
        """test if follow-button is disbled when I click on myself!"""
        login_button = self.driver.find_element(By.ID, "log_in");
        login_button.click();
        
        username = self.driver.find_element(By.NAME, "username");
        username.send_keys("Gretel");
        
        password = self.driver.find_element(By.NAME, "password");
        password.send_keys("1234");
        
        login_button = self.driver.find_element(By.CLASS_NAME, "btn.btn-primary");
        login_button.click();
        
        
        self.driver.get("http://127.0.0.1:8000/profile/Gretel")
        time.sleep(2);
        
        follow_button = self.driver.find_element(By.ID, "follow-btn");
        
        self.assertFalse(follow_button.is_enabled());
        
    def test_following(self):
        self.login(); 
        self.go_to_following();
        
        try:
            first_post = self.driver.find_element(By.CLASS_NAME, "posts");
        except NoSuchElementException:
            first_post = None;
        finally:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_elements(By.CLASS_NAME, "posts")[4]);        
            time.sleep(3);
            self.assertIsNotNone(first_post);
            self.assertGreaterEqual(len(self.driver.find_elements(By.CLASS_NAME, "posts")), 5);
        
        
        
        
        
        