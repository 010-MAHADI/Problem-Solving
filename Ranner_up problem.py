def se_hi(number):
    unic_num = list(set(number))
    unic_num.sort(reverse=True)
    return unic_num[1]


n = int(input())
user = map(int,input().split())
runner_up = se_hi(user)
print(runner_up)
