import os
import subprocess
import unittest

from graphene.test import Client

from flask_graphene.api.schema import schema


class ReadingsTestCase(unittest.TestCase):
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

    def test_all_readings(self):
        client = Client(schema)
        executed = client.execute("""{ allReadings(sort: readingid_asc, first: 1) { edges { node { id } } } }""")
        self.assertEqual(executed,
                         {"data": {"allReadings": {"edges": [ {"node": {"id": "UmVhZGluZ05vZGU6MQ=="} } ] } } })

    def test_reading(self):
        client = Client(schema)
        executed = client.execute("""{ reading(id: "UmVhZGluZ05vZGU6MQ==") { readingid } }""")
        self.assertEqual(executed,
                         {"data": {"reading": {"readingid": "1"} } })


class DevicesTestCase(unittest.TestCase):
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

    def test_all_devices(self):
        client = Client(schema)
        executed = client.execute("""{ allDevices(sort: deviceid_asc, first: 1) { edges { node { id } } } }""")
        self.assertEqual(executed,
                         {"data": {"allDevices": {"edges": [ {"node": {"id": "RGV2aWNlTm9kZTox"} } ] } } })

    def test_device(self):
        client = Client(schema)
        executed = client.execute("""{ device(id: "RGV2aWNlTm9kZTox") { deviceid } }""")
        self.assertEqual(executed,
                         {"data": {"device": {"deviceid": "1"} } })
