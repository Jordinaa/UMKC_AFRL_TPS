# Use an appropriate base image. Ubuntu 20.04 LTS is commonly used for such applications.
FROM ubuntu:20.04

# Set environment to non-interactive (this will prevent some prompts)
ENV DEBIAN_FRONTEND=noninteractive

# Update & Upgrade system
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Install prerequisites and utilities
RUN apt-get install -y python3 python3-pip python3-dev usbutils

# Install mypavutil and mavproxy
RUN pip3 install pymavlink MAVProxy

# Create an entry script to handle input and output
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
