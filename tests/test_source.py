import unittest
from app.models import Sources

class Source(unittest.TestCase):
    def setUp(self):
        self.source = Sources(
           "Aftenposten",
            "Norges ledende nettavis med alltid oppdaterte nyheter innenfor innenriks, utenriks, sport og kultur.",
            "https://www.aftenposten.no"
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.source,Sources))
        