import json
from pathlib import Path

def test_report_exists():
    """
    Verifies Criterion 1: The summary report must be successfully generated 
    and saved to the exact file path `/app/report.json`.
    """
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_format():
    """
    Verifies Criterion 2: The output file must contain a valid JSON object.
    """
    try:
        with open("/app/report.json", "r") as f:
            data = json.load(f)
    except Exception as e:
        assert False, f"Failed to parse /app/report.json as valid JSON: {e}"
    assert isinstance(data, dict), "The root of the JSON file must be an object/dictionary."


def test_report_keys_and_values():
    """
    Verifies Criterion 3: The JSON object must contain the exact keys 'total_requests', 
    'unique_ips', and 'top_path' with the correct computed metrics.
    """
    with open("/app/report.json", "r") as f:
        data = json.load(f)
        
    # Expected metrics compiled from the ground truth access.log:
    # total_requests: 6 (6 valid log rows)
    # unique_ips: 3 (192.168.0.1, 192.168.0.2, 10.0.0.5)
    # top_path: "/index.html" (occurs 3 times)
    assert "total_requests" in data, "Missing key 'total_requests'"
    assert "unique_ips" in data, "Missing key 'unique_ips'"
    assert "top_path" in data, "Missing key 'top_path'"
    
    assert data["total_requests"] == 6, f"Expected 6 total_requests, got {data['total_requests']}"
    assert data["unique_ips"] == 3, f"Expected 3 unique_ips, got {data['unique_ips']}"
    assert data["top_path"] == "/index.html", f"Expected top_path to be '/index.html', got '{data['top_path']}'"
