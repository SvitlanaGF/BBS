from bbs import BBS

n = BBS()

m = n.encrypt('text here')
print(m)
print(n.decrypt(m))
