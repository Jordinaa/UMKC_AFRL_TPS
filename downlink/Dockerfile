FROM python:3.8-slim

WORKDIR /downlink

# Optional: Declare a volume (this is more for documentation and isn't strictly necessary)
VOLUME /downlink/src
VOLUME /downlink/tests

# Optional: Expose a port (e.g., if your script starts a server on port 8080)
# EXPOSE 8080

COPY . .

RUN pip3 install --no-cache-dir -r src/requirements.txt

# ENTRYPOINT ["python3", "-u", "src/mavlink_information.py"]





# TESTS
# ENTRYPOINT ["python3", "-u", "tests/one_param.py"]
# ENTRYPOINT ["python3", "-u", "tests/test_mavlink.py"]

# ENTRYPOINT ["python3", "-u", "tests/list_params.py"]