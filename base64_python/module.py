class Base64:

    def __init__(self):
        self._base64 = []
        for i in range(0,26):
            self._base64.append(chr(65+i))
        for i in range(0,26):
            self._base64.append(chr(97+i))
        for i in range(0,10):
            self._base64.append(str(i))
        self._base64.append("+")
        self._base64.append("/")
    
    def encode(self, data:str|bytes) -> str:
        """
        This function is an encoder function
        Encode a string|bytes to base64.
        """
        try:
            ord_data = data if isinstance(data, bytes) else data.encode("utf-8")
            bin_data = [bin(i) for i in ord_data]
            bin_data = ["0" * (8 - len(i[2:])) + i[2:] if len(i[2:]) != 8 else i[2:] for i in bin_data]
            str_data = "=" * abs(3 - len(bin_data) % 3) if len(bin_data) % 3 != 0 else ""
            bin_data = "".join(bin_data)
            bin_data = [bin_data[i:i+6] for i in range(0, len(bin_data), 6)]
            bin_data = [i + "0" * (6 - len(i)) if len(i) != 6 else i for i in bin_data]
            int_data = [int(i, 2) for i in bin_data]
            return "".join([self._base64[i] for i in int_data]) + str_data if data else ""
        except Exception as e:
            raise e

    def decode(self, data:str|bytes) -> str:
        """
        This is a decoder function
        Decodes a base64 encoded string|bytes.
        """
        try:
            ord_data = data.decode("utf-8") if isinstance(data, bytes) else data
            int_data = [self._base64.index(i) for i in ord_data if i != "="]
            bin_data = [bin(i) for i in int_data]
            bin_data = ["0" * (6 - len(i[2:])) + i[2:] if len(i[2:]) != 6 else i[2:] for i in bin_data]
            bin_data = "".join(bin_data)
            bin_data = [bin_data[i:i+8] for i in range(0, len(bin_data), 8)]
            int_data = [int(i, 2) for i in bin_data]
            ord_data = bytearray(int_data)
            return ord_data.decode("utf-8")
        except Exception as e:
            raise e

class Base64_Url:
    def __init__(self):
        self._base64 = []
        for i in range(0,26):
            self._base64.append(chr(65+i))
        for i in range(0,26):
            self._base64.append(chr(97+i))
        for i in range(0,10):
            self._base64.append(str(i))
        self._base64.append("-")
        self._base64.append("_")
    
    def encode(self, data:str|bytes) -> str:
        """
        This function is an encoder function
        Encode a string|bytes to base64.
        """
        try:
            ord_data = data if isinstance(data, bytes) else data.encode("utf-8")
            bin_data = [bin(i) for i in ord_data]
            bin_data = ["0" * (8 - len(i[2:])) + i[2:] if len(i[2:]) != 8 else i[2:] for i in bin_data]
            bin_data = "".join(bin_data)
            bin_data = [bin_data[i:i+6] for i in range(0, len(bin_data), 6)]
            bin_data = [i + "0" * (6 - len(i)) if len(i) != 6 else i for i in bin_data]
            int_data = [int(i, 2) for i in bin_data]
            return "".join([self._base64[i] for i in int_data])
        except Exception as e:
            raise e

    def decode(self, data:str|bytes) -> str:
        """
        This is a decoder function
        Decodes a base64 encoded string|bytes.
        """
        try:
            ord_data = data.decode("utf-8") if isinstance(data, bytes) else data
            int_data = [self._base64.index(i) for i in ord_data]
            bin_data = [bin(i) for i in int_data]
            bin_data = ["0" * (6 - len(i[2:])) + i[2:] if len(i[2:]) != 6 else i[2:] for i in bin_data]
            bin_data = "".join(bin_data)
            bin_data = [bin_data[i:i+8] for i in range(0, len(bin_data), 8)]
            int_data = [int(i, 2) for i in bin_data]
            ord_data = bytearray(int_data)
            return ord_data.decode("utf-8")
        except Exception as e:
            raise e
    
def test(type:int = 0) -> str:
    """
    This is a test function
    """
    from time import time
    start = time()
    base64 = Base64()
    str_data = base64.encode(b"Exam") # or str_data = base64.encode("Exam")
    base64_data = base64.decode(b"RXhhbQ") # or base64_data = base64.decode("RXhhbQ==")
    end = time()
    text1 = f"""+------------------------------------+
| Input Text     : Exam              |
| Encoding       : {str_data}          |
| Decoding       : {base64_data}              |
| Encodeing Type : Base64            |
| Time           : {end - start:.5f} seconds   |
+------------------------------------+\n"""
    from time import time
    start = time()
    base64 = Base64_Url()
    str_data = base64.encode(b"Exam") # or str_data = base64.encode("Exam")
    base64_data = base64.decode(b"RXhhbQ") # or base64_data = base64.decode("RXhhbQ==")
    end = time()
    text2 = f"""+------------------------------------+
| Input Text     : Exam              |
| Encoding       : {str_data}            |
| Decoding       : {base64_data}              |
| Encodeing Type : Base64_Url        |
| Time           : {end - start:.5f} seconds   |
+------------------------------------+"""
    return text1 + text2

if __name__ == "__main__":
    test = test()
    print(test)