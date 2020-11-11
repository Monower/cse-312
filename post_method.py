# we import the request module
import requests

url='https://jsonplaceholder.typicode.com/posts/'
myobj={'username':'I have posted something. Now I want my treat.'}

r=requests.post(url,data=myobj)

a=r.reason
print(a)

if(a=='Created'):
    print('The status code is: ',a)
    print('Response from the server is: '+r.reason)
    print('The message is:'+r.text)
else:
    print('stay home stay safe.')
