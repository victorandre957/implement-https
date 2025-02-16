import http.client
import ssl

# Create custom context
context = ssl.create_default_context()
context.check_hostname = True  # Enforce hostname validation
context.verify_mode = ssl.CERT_REQUIRED  # Mandatory certificate verification

# Load the server's certificate directly
context.load_verify_locations('server.crt')

try:
    conn = http.client.HTTPSConnection(
        'localhost',  # Must match certificate's CN/SAN
        8443,
        context=context,
        timeout=10
    )
    conn.request('GET', '/')
    response = conn.getresponse()
    print(f"Status: {response.status}")
    print(f"Response: {response.read().decode()}")
except Exception as e:
    print(f"Connection failed: {str(e)}")
finally:
    conn.close()