import requests
'''测试其他方法，post, get , put,delete,'''

post = requests.post('http://httpbin.org/post', data={'key':'value'})
print(post.text)
print('- ' * 15)
put = requests.put('http://httpbin.org/put', data={'key':'value'})
print(put.text)
print('-'*15)
delete = requests.delete('http://httpbin.org/delete')
print(delete.text)
print('-'*15)
head = requests.head('http://httpbin.org/get')
print(head.text)
print('-'*15)
option = requests.options('http://httpbin.org/get')
print(option.text)