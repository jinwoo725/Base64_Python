A beginner's base64 encoder/decoder in Python

class Base64<br>
-_encoding(type:string) > type:string<br>
-_decoding(type:string) > type:string

install<br>
-pip install base64_python

Exam<br>
-import base64_python<br>
-base64 = base64_python.Base64()<br>
-print(base64._encoding("test"))<br>
-print(base64._decoding("dGVzdA=="))



