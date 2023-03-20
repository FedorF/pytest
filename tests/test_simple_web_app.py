import os
import sys

import pytest
from fastapi.testclient import TestClient

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from simple_web_app import app
from dto.data_models import BeelineCustomer, ChurnResponse

client = TestClient(app)


def test_app_is_alive():
    response = client.get(
        "/"
    )
    payload = response.json()

    assert response.status_code == 200
    assert payload == {"info": "Pytest demo."}


@pytest.mark.parametrize(
    "customer, expected_response",
    [
        pytest.param(BeelineCustomer(age=51, arpu=100), ChurnResponse(score=0.5), id="Should response 0.5"),
        pytest.param(BeelineCustomer(age=21, arpu=500), ChurnResponse(score=0.1), id="Should response 0.1"),
    ]
)
def test_model_predict(customer, expected_response):
    response = client.post(
        "/predict/",
        json=customer.dict()
    )
    assert response.status_code == 200
    returned_score = ChurnResponse(**response.json())
    assert expected_response == returned_score
