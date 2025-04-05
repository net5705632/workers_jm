import requests
import base64

url = 'https://lucky-term-fea6.tel13339999091.workers.dev/'

try:
    # 发送GET请求获取内容
    response = requests.get(url)
    response.raise_for_status()  # 检查HTTP错误
    
    # 获取Base64编码的内容并去除空白字符
    encoded_content = response.text.strip()
    
    # 进行Base64解码
    decoded_bytes = base64.b64decode(encoded_content)
    
    # 尝试将解码后的字节转换为字符串
    try:
        decoded_content = decoded_bytes.decode('utf-8')
        print("解码后的内容：\n", decoded_content)
    except UnicodeDecodeError:
        print("解码后的内容不是UTF-8文本，原始字节：\n", decoded_bytes)

except requests.exceptions.RequestException as e:
    print(f"请求出错：{e}")
except base64.binascii.Error as e:
    print(f"Base64解码失败：{e}")
