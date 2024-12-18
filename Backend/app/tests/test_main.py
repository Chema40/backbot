from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sales_webhook():
    response = client.post("/webhook", json={"topic": "Sales", "description": "Need help with a client", "method": "Email" })
    assert response.status_code == 200
    assert response.json() == {'message':{'method': 'Email', 'department': 'Sales',
                                'description': 'Inquire about product offerings, pricing, or bulk purchase discounts', 
                                'id': '1'}}

def test_invalid_topic():
    response = client.post("/webhook", json={"topic": "unknown", "description": "Test", "method": "postal mail"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Unsupported department"