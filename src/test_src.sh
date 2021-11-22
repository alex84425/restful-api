echo "test GET!"

echo "test GET! step 1-0: GET true dir"
curl -i  "http://127.0.0.1:5000//home/alex/workplace_alex/interview/api/test_files/"

echo "test GET! step 1-1: GET invaild dir"
curl -i  "http://127.0.0.1:5000//home/alex/workplace_alex/interview/api/test_files123132/"


echo "test GET! step 1-3: GET sort and file file from dir"
curl -i  "http://127.0.0.1:5000//home/alex/workplace_alex/interview/api/test_files/?orderby=size"
curl -i  "http://127.0.0.1:5000//home/alex/workplace_alex/interview/api/test_files/?orderby=lastModified"
curl -i  "http://127.0.0.1:5000//home/alex/workplace_alex/interview/api/test_files/?orderby=fileName"
curl -i  "http://127.0.0.1:5000//home/alex/workplace_alex/interview/api/test_files/?orderby=fileName&orderByDirection=Dscending&filterByName=char"

echo "test GET! step 1-3: GET true file"
curl -i  "http://127.0.0.1:5000//home/alex/workplace_alex/interview/api/test_files/8char.txt"
echo "test GET! step 1-4: GET invaild file"
curl -i  "http://127.0.0.1:5000//home/alex/workplace_alex/interview/api/test_files/18char.txt"


echo "test POST step 2-1: POST true  file"
curl  -X POST -F "file=@/home/alex/workplace_alex/interview/api/test_files/test_upload/upload.txt" 127.0.0.1:5000/home/alex/workplace_alex/interview/api/test_files/
echo "test POST step 2-1: POST invaild file"
curl  -X POST -F "file=@/home/alex/workplace_alex/interview/api/test_files/test_upload/upload.txt" 127.0.0.1:5000/home/alex/workplace_alex/interview/api/test_file/


