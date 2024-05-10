#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import base64

# 特定の長さの倍数にするため空白でデータを埋める関数

def mkpad(s, size):
    s = s.encode("utf-8")       # UTF-8文字列をバイト列に変換する
    pad = b' ' * (size - len(s) % size)     # 特定の長さの倍数にするための空白を生成
    return s + pad


# 暗号化する

def encrypt(password, data):
    # 特定の長さに調節する
    password = mkpad(password, 16)      # 16の倍数にそろえる
    data = mkpad(data, 16)      # バイト列に変換し16の倍数に揃える
    password = password[:16]        # ちょうど16文字に揃える

    # 暗号化
    aes = AES.new(password, mode, iv)
    data_cipher = aes.encrypt(data)
    return base64.b64encode(data_cipher).decode("utf-8")


# 複合化する

def decrypt(password, encdata):
    # パスワードの文字数を調整
    password = mkpad(password, 16)      # 16の倍数に揃える
    password = password[:16]        # ちょうど16文字に揃える

    # 複合化
    aes = AES.new(password, mode, iv)
    encdata = base64.b64decode(encdata)     # 暗号化データをBASE64でデコードしてバイト列に
    data = aes.decrypt(encdata)     # 複合化
    return data.decode("utf-8")

if __name__ == '__main__':
	
	# 暗号化したいデータとパスワードを指定

	message = "自分がしてほしいと思うことをヒトのもするように。"
	password = "xxxxxxxxxx"     # 適当なパスワードを設定
	iv = Random.new().read(AES.block_size)     # 初期化ベクトル(16文字で適当な値を設定)
	mode = AES.MODE_CBC     # 暗号化モードを指定
	
	# 暗号化する
	enc = encrypt(password,message)
	print("暗号化", enc)

	# 複合化する
	dec = decrypt(password,enc)
	print("複合化", dec)
