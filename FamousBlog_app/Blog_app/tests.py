from django.test import TestCase

class BlogTest(TestCase):
    def test_main(self):
        response = self.client.get("/option")
        self.assertEqual(response.status_code, 3000)