import sys
import os
import unittest
from unittest.mock import patch, MagicMock


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from server_processing import ProcessingHandler  

class TestServerProcessing(unittest.TestCase):

    @patch("server_processing.capture_screenshot", return_value="base64data")
    @patch("server_processing.measure_performance", return_value={
        "load_time_ms": 100,
        "total_size_kb": 200,
        "num_requests": 10
    })
    @patch("server_processing.serialize_result", side_effect=lambda x: b"response")
    @patch("server_processing.deserialize_result", return_value={"url": "http://example.com"})
    def test_handle_success(self, mock_deserialize, mock_serialize, mock_measure, mock_capture):

        mock_request = MagicMock()
        serialized_request = b"abcd"
        msg_len = len(serialized_request).to_bytes(4, "big")
        mock_request.recv.side_effect = [msg_len, serialized_request]

        handler = ProcessingHandler(request=mock_request, client_address=None, server=None)
        handler.handle()

        self.assertGreaterEqual(mock_serialize.call_count, 1)
        first_call = mock_serialize.call_args_list[0][0][0]
        self.assertEqual(first_call["status"], "success")
        self.assertGreaterEqual(mock_request.sendall.call_count, 1)

    @patch("server_processing.capture_screenshot", return_value="")
    @patch("server_processing.measure_performance", return_value={
        "load_time_ms": 0,
        "total_size_kb": 0,
        "num_requests": 0
    })
    @patch("server_processing.serialize_result", side_effect=lambda x: b"response")
    @patch("server_processing.deserialize_result", return_value={"html": "<html></html>"})
    def test_handle_missing_url(self, mock_deserialize, mock_serialize, mock_measure, mock_capture):
    
        mock_request = MagicMock()
        serialized_request = b"abcd"
        msg_len = len(serialized_request).to_bytes(4, "big")
        mock_request.recv.side_effect = [msg_len, serialized_request]
        handler = ProcessingHandler(request=mock_request, client_address=None, server=None)
        handler.handle()

        self.assertGreaterEqual(mock_request.sendall.call_count, 1)

        all_calls = b"".join(call[0][0] for call in mock_request.sendall.call_args_list)
        self.assertIn(b"response", all_calls)  # usa el valor del side_effect

        self.assertGreaterEqual(mock_serialize.call_count, 1)


if __name__ == "__main__":
    unittest.main()