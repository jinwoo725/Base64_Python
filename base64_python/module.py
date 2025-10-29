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
    
    def _encoding(self, data:str) -> str:
        try:
            ord_data = data.encode("utf-8")
            bin_data = [bin(i) for i in ord_data]
            bin_data = [i.replace("0b","") for i in bin_data]
            bin_data = ["0" * abs(len(i)-8) + i if len(i) != 8 else i for i in bin_data]
            bin_data = [bin_data[i:i+3] for i in range(0, len(bin_data), 3)]
            int_data = [self._split(i) for i in bin_data]
            str_data = "=" * abs(len(int_data[-1]) - 4)
            int_data = [j for i in int_data for j in i]
            return "".join([self._base64[i] for i in int_data]) + str_data
        except:
            return ""

    def _decoding(self, data:str) -> str:
        int_data = [self._base64.index(i) for i in data if i != "="]
        bin_data = [bin(i) for i in int_data]
        bin_data = [i.replace("0b","") for i in bin_data]
        bin_data = ["0" * abs(len(i)-6) + i if len(i) != 6 else i for i in bin_data]
        bin_data = "".join(bin_data)
        bin_data = [bin_data[i:i+8] for i in range(0, len(bin_data), 8)]
        int_data = [int(i, 2) for i in bin_data]
        ord_data = bytearray(int_data)
        return ord_data.decode("utf-8")
    
    def _split(self, data:str) -> str:
        bin_data = "".join(data)
        bin_data = [bin_data[i:i+6] for i in range(0, len(bin_data), 6)]
        bin_data = ["0b" + i + "0" * abs(len(i)-6) if len(i) != 6 else "0b" + i for i in bin_data]
        int_data = [int(i,2) for i in bin_data]
        return int_data
    

if __name__ == "__main__":
    base64 = Base64()
    print(base64._encoding("test"))
    print(base64._decoding("dGVzdA=="))