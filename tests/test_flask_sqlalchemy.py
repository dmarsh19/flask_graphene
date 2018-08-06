import unittest

from flask_graphene import db
from flask_graphene.api.models import Reading, Device


class ReadingTestCase(unittest.TestCase):
    MODEL = Reading
    def test_query_all(self):
        results = self.MODEL.query.all()
        self.assertIsInstance(results, list)
        # not empty
        self.assertTrue(results)

    def test_query_get(self):
        result = self.MODEL.query.get(1)
        self.assertEqual(result.temperature, 75.56) 
        self.assertEqual(result.humidity, 61.9)


class DeviceTestCase(unittest.TestCase):
    MODEL = Device
    def test_query_all(self):
        results = self.MODEL.query.all()
        self.assertIsInstance(results, list)
        # not empty
        self.assertTrue(results)

    def test_query_get(self):
        result = self.MODEL.query.get(1)
        self.assertEqual(result.manufacturer, "adafruit")
        self.assertEqual(result.model, "DHT22")

