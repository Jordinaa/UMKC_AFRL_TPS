Downlink

# Directions
'''
docker build -t downlink .
docker run --network host --privileged downlink
docker run --device=/dev/ttyUSB0 downlink
'''

TODO
- [ ] add 33 parameters for mavlink
- [ ] compile IADSInterface