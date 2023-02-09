import unittest

from synth_forc.cli.response import Response


class MyTestCase(unittest.TestCase):

    def test_create_from_json_01(self):
        response = Response(json='{"status": "SUCCESS", "forc_png": "forc.png", "forc_loop_png": "forc-loop.png", "message": "Test message"}')

        self.assertIsInstance(response.status, Response.Status)
        self.assertEqual(response.status, Response.Status.SUCCESS)
        self.assertEqual(response.forc_png, "forc.png")
        self.assertEqual(response.forc_loop_png, "forc-loop.png")
        self.assertEqual(response.message, "Test message")
        self.assertIsNone(response.exception)

    def test_create_from_json_02(self):
        response = Response(json='{"status": "SUCCESS", "forc_png": "forc.png", "forc_loop_png": "forc-loop.png", "message": "Test message", "exception": "Test exception"}')

        self.assertIsInstance(response.status, Response.Status)
        self.assertEqual(response.status, Response.Status.SUCCESS)
        self.assertEqual(response.forc_png, "forc.png")
        self.assertEqual(response.forc_loop_png, "forc-loop.png")
        self.assertEqual(response.message, "Test message")
        self.assertEqual(response.exception, "Test exception")

    def test_create_from_json_03(self):
        response = Response(json='{"status": "EMPTY_BINS", "message": "Empty bins when calculating distribution weights.", "forc_png": "", "forc_loop_png": "", "exception": ""}')

        self.assertIsInstance(response.status, Response.Status)
        self.assertEqual(response.status, Response.Status.EMPTY_BINS)
        self.assertEqual(response.forc_png, "")
        self.assertEqual(response.forc_loop_png, "")
        self.assertEqual(response.message, "Empty bins when calculating distribution weights.")
        self.assertEqual(response.exception, "")

    def test_create_from_parameters_01(self):
        response = Response(status="SUCCESS", forc_png="forc.png", forc_loop_png="forc-loop.png", message="Test message")

        self.assertIsInstance(response.status, Response.Status)
        self.assertEqual(response.status, Response.Status.SUCCESS)
        self.assertEqual(response.forc_png, "forc.png")
        self.assertEqual(response.forc_loop_png, "forc-loop.png")
        self.assertEqual(response.message, "Test message")
        self.assertIsNone(response.exception)


if __name__ == '__main__':
    unittest.main()
