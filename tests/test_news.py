import unittest
from app.models import Articles

class ArticleTest (unittest.TestCase):
    '''
    Test class to test the behavior of the movie
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.articles = Articles(
            "New York Times",
            "Marc Santora, Ivan Nechepurenko",
            "Russia-Ukraine War Live Updates: Odesa Airport and Mariupol News - The New York Times",
            "The House speaker announced that she had met with President Volodymyr Zelensky on Saturday in Kyiv. She is the highest ranking U.S. official to travel to Ukraine since the war began.",
            "https://www.nytimes.com/live/2022/05/01/world/ukraine-russia-war-news",
            "https://static01.nyt.com/images/2022/05/01/world/01ukraine-blog-promo-6am-EST/01ukraine-blog-promo-6am-EST-facebookJumbo.jpg",
            "2022-05-01T10:25:58Z",
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.articles,Articles))
        

