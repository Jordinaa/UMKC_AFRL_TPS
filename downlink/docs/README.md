Downlink

# Directions
'''
docker build -t downlink .
docker run --network host --privileged downlink
docker run --network host --privileged -it downlink /bin/bash
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