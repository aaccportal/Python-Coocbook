# 6.2. Reading and Writing JSON Data

# Problem
# You want to read or write data encoded as JSON (JavaScript Object Notation).

# Solution
# The json module provides an easy way to encode and decode data in JSON. The two
# main functions are json.dumps() and json.loads(), mirroring the interface used in
# other serialization libraries, such as pickle. Here is how you turn a Python data structure
# into JSON:

# Проблема
# Вы хотите читать или записывать данные, закодированные как JSON (обозначение объектов JavaScript).

# Решение
# Модуль json предоставляет простой способ кодирования и декодирования данных в формате JSON. Два
# основными функциями являются json.dumps() и json.loads(), отражающие интерфейс, используемый в
# другие библиотеки сериализации, такие как pickle. Вот как вы превращаете структуру данных Python
# в JSON:

import json
data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}
json_str = json.dumps(data)
print(json_str)

# Here is how you turn a JSON-encoded string back into a Python data structure:
# Вот как вы превращаете строку в кодировке JSON обратно в структуру данных Python:

data = json.loads(json_str)
print(data)

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)
    
# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)