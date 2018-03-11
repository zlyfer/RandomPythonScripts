import hashlib
while 1:
    success = False
    text = input("text: ")
    type = str(input("type (sha1, md5): "))
    if type == "sha1":
        hash = hashlib.sha1()
        success = True
    elif type == "md5":
        hash = hashlib.md5()
        success = True
    else:
        print ("Type %s not supported.\n" % type)
    if success:
        hash.update(str(text).lower().encode('utf-8'))
        print("%s\n" % hash.hexdigest())