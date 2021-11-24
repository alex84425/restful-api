# Build restful-api using sanic and flask



## Description

Build restful-api to acess filesystem and support asyncio.

## Getting Started

### Dependencies

* linux

### How to install

* step 1:
```
git clone https://github.com/alex84425/restful-api.git
```
* step 2:
  * option1 :
```
pip install -r requirements.txt
```

  * option2 : get docker image by Dockerfile
```
cd src/
docker build --build-arg INCUBATOR_VER=20160613.3  -t api ./
```



# How to run:

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

  * option 1: run locally
```
python  src/rest-api_sanic.py --root_path /home/alex/workplace_alex/interview/api/ --port 5001 --w 1
```

  * option 2: run with docker
```
docker run -it --name sanic  --network host  api  python /restful-api/src/rest-api_sanic.py --root_path / --port 5000 --host "127.0.0.1"
```

  * option 3: run with docker-compose, parameters such as port and host should be edited in Dockerfile before build image.
```
docker-compose up
```

# test unit test:

###  Request GET - if the request target is dir.
* GET existed dir
```
curl -i  "http://127.0.0.1:5000/restful-api/test_files/"
```
![image](https://user-images.githubusercontent.com/26201458/143234292-4db9c789-8f7c-4cad-9c8b-22b51350f2d9.png)

* GET existed dir with parameter
```
curl -i  "http://127.0.0.1:5000/restful-api/test_files/?orderby=fileName&orderByDirection=Descending&filterByName=char"
```
![image](https://user-images.githubusercontent.com/26201458/143230782-2777ccfa-03ed-4a99-acf8-833ea5a821aa.png)


* GET invaid dir
```
curl -i  "http://127.0.0.1:5000/restful-api/test_files_invaild/"
```
![image](https://user-images.githubusercontent.com/26201458/143230619-61dd35d9-c76e-4431-90bc-71dd8bae5e5d.png)


###  Request GET - if the request target is file.

* GET existed file and return binary stream
```
curl -i  "http://127.0.0.1:5000/restful-api/test_files/32char.txt"
```
![image](https://user-images.githubusercontent.com/26201458/143230997-f528382a-2d9b-4359-8023-fde402455eba.png)

* GET invaild file and return error
```
curl -i  "http://127.0.0.1:5000/restful-api/test_files/fake.txt"
```
![image](https://user-images.githubusercontent.com/26201458/143231058-f10f4bd7-3c40-46eb-ac1b-1632d505a73f.png)

###  Request POST - target should be dir with key[file], if file existed not allow to operate.
```
curl  -X POST -F "file=@/home/alex/workplace_alex/interview/api/test_files/test_upload/upload.txt"  "http://127.0.0.1:5000/restful-api/test_files/test_upload/"
```
###  Request PATCH - target should be dir with key[file], only allow to operate with existed file.
```
curl  -X PATCH -F "file=@/home/alex/workplace_alex/interview/api/test_files/test_upload/upload.txt"  "http://127.0.0.1:5000/restful-api/test_files/test_upload/"
```

![image](https://user-images.githubusercontent.com/26201458/143231591-a9e90b65-73e0-4538-a1fe-2f1090e8a24b.png)
###  Request DELETE - remove target file or dir
DEL single file
```
#check
curl  -X POST -F "file=@/home/alex/workplace_alex/interview/api/test_files/test_upload/upload.txt"  "http://127.0.0.1:5000/restful-api/test_files/test_DEL/"
curl -i  "http://127.0.0.1:5000/restful-api/test_files/test_DEL/"
curl  -X DELETE  "http://127.0.0.1:5000/restful-api/test_files/test_DEL/upload.txt"
curl -i  "http://127.0.0.1:5000/restful-api/test_files/test_DEL/"
```
![image](https://user-images.githubusercontent.com/26201458/143240357-b7178edb-b923-451b-bacb-9760c11a17fb.png)

DEL single dir
```
curl  -X POST -F "file=@/home/alex/workplace_alex/interview/api/test_files/test_upload/upload.txt"  "http://127.0.0.1:5000/restful-api/test_files/test_DEL/"
curl -i  "http://127.0.0.1:5000/restful-api/test_files/test_DEL/"
curl  -X DELETE  "http://127.0.0.1:5000/restful-api/test_files/test_DEL/"
curl -i  "http://127.0.0.1:5000/restful-api/test_files/test_DEL/"
```

![image](https://user-images.githubusercontent.com/26201458/143240737-18f62796-700d-4a2c-9c7b-5d45d12d4ade.png)


## Help



## Version History

* 0.1
    * Initial Release

