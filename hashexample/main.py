import hashlib # importing module

def hash(data): # creating a function that will get argument and then use it to hash it
    return hashlib.sha256(data.encode()).hexdigest() # returns a hash from data, there are actually many types of hashing, you read them on internet
    # we are encoding data we got, and then calling a function hexdigest(), to get the final result

print(hash("Hello, World!")) # printing hashed "Hello, World!" using our function that we declared before

# Output:
# dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f