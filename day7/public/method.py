import hashlib
#加密密码函数
def encryptpass(args):
    pas = hashlib.sha256()
    pas.update(args.encode())
    return pas.hexdigest()
