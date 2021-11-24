# Build restful-api using sanic and flask

Simple overview of use/purpose.

## Description

Build restful-api to acess filesystem and support asyncio.

## Getting Started

### Dependencies

* linux

### Installing

* step 1:
```
git clone https://github.com/alex84425/restful-api.git
```
* step 2:
option1 :
```
pip install -r requirements.txt
```

option2 : get docker image by Dockerfile
```
cd src/
docker build --build-arg INCUBATOR_VER=20160613.3  -t api ./
```



### Executing program

* basic instruction
```
usage: rest-api_sanic.py [-h] [--root_path ROOT_PATH] [-d] [--host [HOST]] [--port [PORT]]
                         [--w [W]]

optional arguments:
  -h, --help            show this help message and exit
  --root_path ROOT_PATH
                        Path to serve.
  -d, --debug           Run in debug mode.
  --host [HOST]         Host to bind to.
  --port [PORT]         Port to listen on.
  --w [W]               worker num

```
* How to run:
option 1: run locally
```
python  src/rest-api_sanic.py --root_path /home/alex/workplace_alex/interview/api/ --port 5001 --w 1
```

option 2: run with docker
```
docker run -it --name sanic  --network host  api  python /restful-api/src/rest-api_sanic.py --root_path / --port 5000 --host "127.0.0.1"
```

option 3: run with docker-compose, parameter such as port should be edited in Dockerfile before build image.
```
docker-compose up
```


## Help

s://twitter.com/dompizzie)

## Version History

* 0.1
    * Initial Release

