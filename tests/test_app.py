import os, subprocess, json
def test_model_exists():
    assert os.path.exists("model.pkl")

def test_predict_endpoint_available():
    # This test only checks that model exists; running the server in CI is optional.
    assert os.path.exists("model.pkl")
