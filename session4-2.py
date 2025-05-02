import random
def main():
    print("Chào mừng bạn đã đến với Xỉu cùng Tài 101")
    print("Bạn được tặng 100.000VND vào tài khoản")
    account = 100000

    print("\nBạn có muốn nạp không?")
    print("1. Có\n2. Không")
    money_choice = input("Bạn chọn: ")
    
    if money_choice == '1':    
        add_from_bank = int(input("\nNhập số tiền bạn muốn nạp: "))
        account += add_from_bank
        print(f"Nạp hoàn tất!\nSố tiền trong tài khoản của bạn hiện là {account}")

    try:
        money = int(input("\nNhập số tiền bạn muốn đặt cược: "))
        
        while money > account:
            print("Số tiền đặt cược phải nhỏ hơn Số tiền trong tài khoản")
            money = int(input("Nhập lại số tiền bạn muốn đặt cược: "))

        while money < 1000:
            print("Số tiền đặt cược phải lớn hơn 1000")
            money = int(input("Nhập lại số tiền bạn muốn đặt cược: "))
        
    except:
        print("Số tiền bạn nhập không đúng")

    guess = user_guess()
    money_result = game_engine(guess, money)
    account += money_result
    print(f"Số tiền trong tài khoản của bạn hiện là {account}")

def game_engine(guess, money):
    face1 = random.randint(1,7)
    face2 = random.randint(1,7)
    sum_faces = face1 + face2
    result = ''

    if sum_faces > 5:
        result = 't'
        print("Tài")
    else:
        result = 'x'
        print("Xỉu")

    print(f"Kết quả là {face1} {face2} {sum_faces}")
    if result == guess:
        print("Chúc mừng bạn đã chiến thắng! ")
        print(f"Tài khoản: +{money}")
        return money*2
    else: 
        print("Tiếc quá, bạn thua mất rồi!")
        print(f"Tài khoản: -{money}")
        return -money

def user_guess():
    print("Bạn chọn Tài hay Xỉu:\n1. Tài\n2. Xỉu")
    guess = int(input('Mời bạn chọn: '))

    while guess == 1 or guess == 2:
        if guess == 1:
            return 't'
        elif guess == 2:
            return 'x'
        else:
            guess = int(input('Mời bạn nhập lại: '))

def add_money(account):
    pass

main()