Base64_Python<br>
-

A beginner's base64/base64_Url encoder/decoder in Python

install<br>
-
Linux&MacOS
-
**Bash/Zsh**
```bash
pip3 install base64_python
```
Windows
-
**CMD/PowerShell**
```cmd
pip install base64_python
```

function<br>
-
- **Base64.encode(str|bytes) -> str**<br>
- **Base64.decode(str|bytes) -> str**<br>
- **Base64_Url.encode(str|bytes) -> str**<br>
- **Base64_Url.decode(str|bytes) -> str**<br>
- **test() -> str**

Exam<br>
-
**Example**<br>
```python
import base64_python
base64 = base64_python.Base64()
base64_url = base64_python.Base64_Url()
print(base64.encode("Exam"))
print(base64.decode("RXhhbQ=="))
print(base64_url.encode("Exam"))
print(base64_url.decode("RXhhbQ"))
print(base64_python.test())
```
**Output**<br>
```output
RXhhbQ==
Exam
RXhhbQ
Exam
+------------------------------------+
| Input Text     : Exam              |
| Encoding       : RXhhbQ==          |
| Decoding       : Exam              |
| Encodeing Type : Base64            |
| Time           : 0.00004 seconds   |
+------------------------------------+
+------------------------------------+
| Input Text     : Exam              |
| Encoding       : RXhhbQ            |
| Decoding       : Exam              |
| Encodeing Type : Base64_Url        |
| Time           : 0.00003 seconds   |
+------------------------------------+
```

License<br>
-

This project is licensed under the terms of the MIT license.