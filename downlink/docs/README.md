Downlink

# Directions
```
docker build -t downlink .
docker run --network host --privileged downlink
docker run --network host --privileged -it downlink /bin/bash

docker run -v $(pwd)/src:/downlink/src -v $(pwd)/tests:/downlink/tests downlink
```

**RUNNING TESTS**
```
docker exec -it DOCKERC /bin/bash
cd tests/
python3 
```

make sure ip in python script is target machines correct ip address

**Clean up docker containers**
```
docker rm $(docker ps -q -f status=exited)
docker rmi $(docker images -q)
docker system prune -a 
```


