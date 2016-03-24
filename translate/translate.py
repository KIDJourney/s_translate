import requests

def translate(word, key, fromkey, doctype):
    url = "http://fanyi.youdao.com/openapi.do?keyfrom={0}&key={1}&type=data&doctype={2}&version=1.1&q=要翻译的文本"