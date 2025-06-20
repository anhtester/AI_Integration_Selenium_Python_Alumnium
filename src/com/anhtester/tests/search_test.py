import os
import warnings
from dotenv import load_dotenv
import unittest
from alumnium import Alumni, Model
from selenium.webdriver import Chrome

load_dotenv()
warnings.filterwarnings("ignore")


class TestSearchUseSelenium(unittest.TestCase):
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

    def setUp(self):
        self.driver = Chrome()
        self.driver.maximize_window()
        self.driver.get("https://anhtester.com")
        self.driver.implicitly_wait(10)
        self.al = Alumni(self.driver, model=Model(provider="google", name="gemini-2.0-flash"))

    def test_search_blog(self):
        self.al.do("Click on menu BLOG")
        self.al.do("Search a post name is 'Prompt để hỏi Chat AI trong Software Testing Automation'")
        self.al.check("The post title 'Prompt để hỏi Chat AI trong Software Testing Automation' is displayed")
        post_name = self.al.get("first post name")
        print(f"\n" + post_name)
        self.assertIn(post_name, "123 Prompt để hỏi Chat AI trong Software Testing Automation")

    def test_search_course(self):
        self.al.do("Click input search course in home page section")
        self.al.do("Fill a course name is 'Khoá học Python dành cho Tester'")
        self.al.do("Submit search form")
        self.al.check("The course name 'Khoá học Python dành cho Tester' is displayed")
        course_name = self.al.get("first course name")
        print(f"\n" + course_name)
        self.assertIn(course_name, "Khoá học Python dành cho Tester")

    def tearDown(self):
        self.al.quit()
        self.driver.quit()
