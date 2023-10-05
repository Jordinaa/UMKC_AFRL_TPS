Downlink

# Directions
'''
docker build -t downlink .
docker run --network host --privileged downlink
docker run --device=/dev/ttyUSB0 downlink
'''

**Clean up docker containers**
'''
docker rm $(docker ps -q -f status=exited)
docker rmi $(docker images -q)
docker system prune -a
'''

TODO
- [ ] add 33 parameters for mavlink
- [ ] compile IADSInterface