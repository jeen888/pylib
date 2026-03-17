import secrets

key = secrets.token_hex(16) # 1byte는 2자리의 16진수로 표현되므로, 16byte는 32자리의 16진수로 표현됩니다.
key4 = secrets.token_hex(4) # 4byte는 8자리의 16진수로 표현됩니다.
print(key)
print(key4)
