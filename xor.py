import base64

class StringFogImpl:
    CHARSET_NAME_UTF_8 = "UTF-8"

    @staticmethod
    def decrypt(s, charset_name):
        return StringFogImpl().decrypt(s, charset_name)

    def encrypt(self, s, charset_name):
        try:
            return base64.b64encode(self.xor(s.encode("UTF-8"), charset_name)).decode()
        except UnicodeEncodeError:
            return base64.b64encode(self.xor(s.encode(), charset_name)).decode()

    def decrypt(self, s, charset_name):
        try:
            return self.xor(base64.b64decode(s), charset_name).decode("UTF-8")
        except UnicodeDecodeError:
            return self.xor(base64.b64decode(s), charset_name).decode()

    def overflow(self, s, _):
        return s is not None and (len(s) * 4) / 3 >= 65535

    @staticmethod
    def xor(b_arr, s):
        length = len(b_arr)
        length2 = len(s)
        i = 0
        i2 = 0

        b_arr = bytearray(b_arr)

        while i2 < length:
            if i >= length2:
                i = 0
            b_arr[i2] = b_arr[i2] ^ ord(s[i])
            i2 += 1
            i += 1

        return bytes(b_arr)
