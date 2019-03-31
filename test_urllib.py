from urllib import request

with request.urlopen('http://127.0.0.1:5000/') as f:
    data = f.read()
    data = str(data)
    if data.find('Sheep') > 0:
        print(data)





