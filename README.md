## Getting Started

Follow these steps to set up and run the project on a Linux system:

### Prerequisites

- Python 3.x installed

### How to run

1. run `python3 -m venv .venv`
2. run `source ./venv/bin/activate`
3. execute `openssl req -x509 -newkey rsa:4096 -sha256 -days 365 -nodes \
  -keyout server.key -out server.crt -subj "/CN=localhost" \
  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"`
4. run `python3 server.py`
5. run `python3 client.py`
