def refund(bill, pay):
    change = pay - bill
    fourKids = int(change / 1000)
    change %= 1000
    deer = int(change / 500)
    change %= 500
    sunWen = int(change / 100)
    change %= 100
    goldCoin = int(change / 50)
    change %= 50
    ten = int(change / 10)
    change %= 10
    five = int(change / 5)
    change %= 5
    one = int(change / 1)
    print(fourKids,'張千元, ', deer, '張五百, ', sunWen, '張百元, ', goldCoin, '個五十元, ', ten, '個十元, ', five, '個五元, ', one, '個一元' )

def enough(bill, pay):
    if bill < pay:
        refund(bill, pay)
    elif bill > pay:
        print('金額不足，請繼續放入紙鈔或硬幣，謝謝')
    else:
        print('謝謝您的光臨！')

def main():
    bill = int(input('請輸入應付金額 NT$'))
    pay = int(input('請輸入實際付款金額 NT$'))
    enough(bill, pay)

main()