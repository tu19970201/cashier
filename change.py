# 算出應該找零的數量
def refund(bill, pay):
    change = pay - bill
    currency = [1000,500,100,50,10,5,1] # 所有法幣的幣值
    num = []
    print('找零為', change, '元')
    # 利用迴圈從最大的幣值開始除，若該幣值需找零，則列印出數字
    for c in currency:
        n = int(change / c)
        num.append(n)
        change %= c
        if n > 0:
            print(c, '元 X', n)

# 判斷是否需找零
def enough(bill, pay):
    if bill < pay:
        refund(bill, pay)
    elif bill > pay:
        print('金額不足，請繼續放入紙鈔或硬幣，謝謝')
    else:
        print('謝謝您的光臨！')

# main
def main():
    bill = int(input('請輸入應付金額 NT$'))
    pay = int(input('請輸入實際付款金額 NT$'))
    enough(bill, pay)

main()