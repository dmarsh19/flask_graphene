import os
import subprocess
import unittest

from flask_graphene import db
from flask_graphene.api.models import Reading, Device


class ReadingTestCase(unittest.TestCase):
    MODEL = Reading
    TEST_DB = "atmo.sqlite"

    @classmethod
    def setUpClass(cls):
        with open(cls.TEST_DB, 'wb') as f:
            completed_proc = subprocess.run(["gunzip", "-c", "atmo.sqlite.gz"], stdout=f)
        if completed_proc.returncode != 0:
            raise Exception("failed to gunzip test data.")

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.TEST_DB)

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
    TEST_DB = "atmo.sqlite"

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.TEST_DB)

    @classmethod
    def setUpClass(cls):
        with open(cls.TEST_DB, 'wb') as f:
            completed_proc = subprocess.run(["gunzip", "-c", "atmo.sqlite.gz"], stdout=f)
        if completed_proc.returncode != 0:
            raise Exception("failed to gunzip test data.")

    def test_query_all(self):
        results = self.MODEL.query.all()
        self.assertIsInstance(results, list)
        # not empty
        self.assertTrue(results)

    def test_query_get(self):
        result = self.MODEL.query.get(1)
        self.assertEqual(result.manufacturer, "adafruit")
        self.assertEqual(result.model, "DHT22")

