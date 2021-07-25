from django.test import LiveServerTestCase;
from selenium import webdriver;
from selenium.webdriver.common.by import By;

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
        self.login();
        
        all_nav_bar_names = []; 
        all_posts = self.driver.find_elements(By.TAG_NAME, "li");

        
        for listitem in all_posts:
            all_nav_bar_names.append(listitem.text);
                   
        assert "New Post" in all_nav_bar_names;
        
    def test_send(self):
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
        self.login();
        
        all_posts_nav = self.driver.find_element(By.ID, "all_posts");
        all_posts_nav.click();
        
        post_div = self.driver.find_element(By.ID, "compose-posts");
        
        self.assertEqual(post_div.text, "Posts to show");
        
    def test_posts_json(self):    
        
        self.login();
        
        all_posts_nav = self.driver.find_element(By.ID, "all_posts");
        all_posts_nav.click();
       
       
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);");
        self.assertEqual(False,True);