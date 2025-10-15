from core.plugins.payload_engine import load_payloads

def test_payloads_loaded():
    payloads = load_payloads("payloads/sql_payloads.txt")
    assert len(payloads) > 0
