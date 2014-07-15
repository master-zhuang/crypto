
m Crypto.Cipher import AES
import struct
import hashlib
import random


def GenerageKey():
    import random
    import struct
    import hashlib
    seeds = random.random()
    m = hashlib.md5()
    m.update(str(seeds))
    ret1 = m.digest()
    seeds = random.random()
    m.update(str(seeds))
    ret2 = m.digest()
    ret = struct.pack("%ds%ds"%(len(ret1),len(ret2)),ret1,ret2)
    return ret
    
print (len(GenerageKey()))



key = GenerageKey()
text = GenerageKey()
obj = AES.new(key)
cryp = obj.encrypt(text)
after = obj.decrypt(cryp)

if after == text:
    print ("success")
