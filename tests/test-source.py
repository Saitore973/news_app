import unittest
from app.models import Source

class test_sources(unittest.TestCase):

    '''
      Test Class to test the behaviour of the Sources class
      '''
    def setUp(self):
          '''
        Set up method that will run before every Test
        '''
          self.new_source = Source('abc-news', 'ABC-news' )

    def test_instance(self):
        self.assertTrue(self.new_source, Source)