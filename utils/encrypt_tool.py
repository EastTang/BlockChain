from Crypto.Cipher import DES


class DESUtils:
    _KEY = b'CodeTang'
    # ECB 方式
    _GENERATOR = DES.new(_KEY, DES.MODE_ECB)

    @staticmethod
    def encrypt_des(cipher: str):
        """
        :param cipher: 原文 类型 str 方法内会转 utf-8
        :return res: 密文 类型 bytes
        """
        res = cipher
        try:
            # 加密
            original_text_utf = cipher.encode('utf-8')
            # 非 8 整数倍 空格补齐
            pad_str = chr(1) * (8 - len(original_text_utf) % 8)
            encrypted = DESUtils._GENERATOR.encrypt(original_text_utf + pad_str.encode('utf-8'))
            # 打印输出
            print('明文: {}\n密文: {}'.format(cipher, encrypted))
            # 结果赋值
            res = encrypted
        except Exception as e:
            print('Exception: ', e)
        finally:
            return res

    @staticmethod
    def decrypt_des(encrypted: bytes):
        """
        :param encrypted: 密文 类型 bytes
        :return res: 明文 类型 str 以通过 utf-8 解码
        """
        res = encrypted
        try:
            res = DESUtils._GENERATOR.decrypt(encrypted).decode('utf-8').strip('')
            print('密文: {}\n明文: {}'.format(encrypted, res))
        except Exception as e:
            print('Exception: ', e)
        finally:
            return res


if __name__ == '__main__':
    pwd_str = '你好 '
    cipher_text = DESUtils.encrypt_des(pwd_str)
    original_text = DESUtils.decrypt_des(cipher_text)
