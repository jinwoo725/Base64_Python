Base64_Python<br>
-

A beginner's base64 encoder/decoder in Python

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
- **encode(str|bytes) -> str**<br>
- **decode(str|bytes) -> str**<br>
- **test() -> str**

Exam<br>
-
**Example**<br>
```python
import base64_python
base64 = base64_python.Base64()
print(base64.encode("Exam"))
print(base64.decode("RXhhbQ=="))
print(base64_python.test())
```
**Output**<br>
```output
RXhhbQ==
Exam
+--------------------------------+
| Input Text : Exam              |
| Encoding   : RXhhbQ==          |
| Decoding   : Exam              |
| Time       : 0.00004 seconds   |
+--------------------------------+
```

License<br>
-


This project is licensed under the terms of the MIT license.
