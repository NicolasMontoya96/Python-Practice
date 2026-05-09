from pwdlib import PasswordHash
pwd_context = PasswordHash.recommended()

print(f"Hash para 123456: {pwd_context.hash('123456')}")
print(f"Hash para 7890: {pwd_context.hash('7890')}")