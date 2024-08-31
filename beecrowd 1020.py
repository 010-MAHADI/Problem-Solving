user = int(input())

year = user // 365
user1 = user % 365
month = user1 // 30
user2 = user1 % 30
day = user2
print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{day} dia(s)")
