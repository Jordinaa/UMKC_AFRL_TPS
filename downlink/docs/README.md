Downlink

# Directions
**to build**
docker build -t downlink .

**to run the container**
docker run --rm -it --privileged -v /dev:/dev downlink -i "IP1,IP2" -p PORT


TODO
- [ ] add 33 parameters for mavlink
- [ ] compile IADSInterface