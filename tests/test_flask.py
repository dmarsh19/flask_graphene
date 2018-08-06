import unittest
from urllib.request import urlopen


class BasePageTestCase(unittest.TestCase):

    def test_base_response(self):
        response = urlopen("http://localhost")
        self.assertEqual(response.getcode(), 200)
        response = urlopen("http://localhost/")
        self.assertEqual(response.getcode(), 200)


class GraphQLPageTestCase(unittest.TestCase):

    def test_graphql_query(self):
        response = urlopen("http://localhost/api/graphql?query={allReadings(sort:readingid_asc,first:1){edges{node{id}}}}")
        self.assertEqual(response.getcode(), 200)
        self.assertEqual(response.read(),
                         b"""{"data":{"allReadings":{"edges":[{"node":{"id":"UmVhZGluZ05vZGU6MQ=="}}]}}}""")

