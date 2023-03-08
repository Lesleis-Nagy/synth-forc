import unittest
import json

from synth_forc.cli.response import Response
from synth_forc.cli.response import ResponseStatusEnum


class MyTestCase(unittest.TestCase):

    def test_create_from_json_01(self):
        response = Response(json.loads('{"status": "SUCCESS", "forc_png": "forc.png", "forc_loop_png": "forc-loop.png", "message": "Test message"}'))

        self.assertEqual(response.status, ResponseStatusEnum.SUCCESS.value)
        self.assertEqual(response.forc_png, "forc.png")
        self.assertEqual(response.forc_loop_png, "forc-loop.png")
        self.assertEqual(response.message, "Test message")
        self.assertIsNone(response.exception)

    def test_create_from_json_02(self):
        response = Response(json.loads('{"status": "SUCCESS", "forc_png": "forc.png", "forc_loop_png": "forc-loop.png", "message": "Test message", "exception": "Test exception"}'))

        self.assertEqual(response.status, ResponseStatusEnum.SUCCESS.value)
        self.assertEqual(response.forc_png, "forc.png")
        self.assertEqual(response.forc_loop_png, "forc-loop.png")
        self.assertEqual(response.message, "Test message")
        self.assertEqual(response.exception, "Test exception")

    def test_create_from_json_03(self):
        response = Response(json.loads('{"status": "EMPTY_BINS", "message": "Empty bins when calculating distribution weights.", "forc_png": "", "forc_loop_png": "", "exception": ""}'))

        self.assertEqual(response.status, ResponseStatusEnum.EMPTY_BINS.value)
        self.assertEqual(response.forc_png, "")
        self.assertEqual(response.forc_loop_png, "")
        self.assertEqual(response.message, "Empty bins when calculating distribution weights.")
        self.assertEqual(response.exception, "")

    def test_create_from_parameters_01(self):
        response = Response()
        response.status = "SUCCESS"
        response.forc_png = "forc.png"
        response.forc_loop_png = "forc-loop.png"
        response.message = "Test message"

        self.assertEqual(response.status, ResponseStatusEnum.SUCCESS.value)
        self.assertEqual(response.forc_png, "forc.png")
        self.assertEqual(response.forc_loop_png, "forc-loop.png")
        self.assertEqual(response.message, "Test message")
        self.assertIsNone(response.exception)


if __name__ == '__main__':
    unittest.main()
