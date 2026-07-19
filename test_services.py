"""
Quick test script to verify all services are responding correctly
"""
import requests
import time

GATEWAY_URL = "http://localhost:8000"

def test_health_checks():
    """Test health endpoints"""
    print("\n🔍 Testing Health Checks...")
    
    endpoints = {
        "Gateway": "http://localhost:8000/health",
        "Sentiment": "http://localhost:8001/health",
        "Resume": "http://localhost:8002/health",
        "Image": "http://localhost:8003/health"
    }
    
    for name, url in endpoints.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✅ {name}: OK")
            else:
                print(f"❌ {name}: Failed (Status {response.status_code})")
        except requests.exceptions.ConnectionError:
            print(f"❌ {name}: Not reachable")
        except Exception as e:
            print(f"❌ {name}: Error - {e}")

def test_sentiment_api():
    """Test sentiment analysis"""
    print("\n🔍 Testing Sentiment Analysis...")
    
    try:
        response = requests.post(
            f"{GATEWAY_URL}/sentiment",
            json={"text": "I love this product!"},
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Sentiment API: {data}")
        else:
            print(f"❌ Sentiment API failed: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"❌ Sentiment API error: {e}")

def test_gateway_routing():
    """Test gateway root endpoint"""
    print("\n🔍 Testing Gateway Routing...")
    
    try:
        response = requests.get(f"{GATEWAY_URL}/", timeout=5)
        if response.status_code == 200:
            print(f"✅ Gateway: {response.json()}")
        else:
            print(f"❌ Gateway failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Gateway error: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("AI Inference Platform - Service Test")
    print("=" * 60)
    
    test_gateway_routing()
    test_health_checks()
    test_sentiment_api()
    
    print("\n" + "=" * 60)
    print("Test Complete!")
    print("=" * 60)
