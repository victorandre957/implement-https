from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('server.crt', 'server.key')

# Enforce modern protocols
context.minimum_version = ssl.TLSVersion.TLSv1_2
context.maximum_version = ssl.TLSVersion.TLSv1_3

# Set secure ciphers
context.set_ciphers('ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384')

server_address = ('localhost', 8443)  # Use localhost for strict validation
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Server running at https://{server_address[0]}:{server_address[1]}")
httpd.serve_forever()