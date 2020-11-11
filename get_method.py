import requests

# we create an object by passing the url into the get method
r=requests.get('https://jsonplaceholder.typicode.com/posts/')

# finally we print our desired method with the object created before.
print("Response Code: ",r.status_code)
print("Message: "+r.reason)
print("GET Response: \n"+r.text)
print(len(r.content))
