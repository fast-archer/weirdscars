# Usage: python cipher.py TRAUMA "your text"
# Prints HEX and HASH to paste into index.html (const HEX=..., HASH=...)
import sys, hashlib
key = sys.argv[1].upper().encode()
text = sys.argv[2].encode('utf-8')
ct = bytes(x ^ key[i % len(key)] for i, x in enumerate(text))
assert bytes(x ^ key[i % len(key)] for i, x in enumerate(ct)) == text
print('HEX  =', ' '.join(f'{x:02X}' for x in ct))
print('HASH =', hashlib.sha256(text).hexdigest())
