import random

def menu():
    print("--------------------------------------MENU--------------------------------------")
    print("1/In ra danh sách vừa tạo.\n"
    "2/In đảo ngược danh sách.\n"
    "3.Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).\n"
    "4.Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.\n" 
    "5.Đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.\n"
    "6.In ra vị trí các phần tử là số nguyên tố.\n" 
    "7.Tìm các số duy nhất (không trùng lặp) trong danh sách.\n"
    "8.Liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.\n"
    "9.In ra các đoạn con trong danh sách giảm liên tiếp.\n"
    "10.Thoát")

    choice = int(input("Nhập thao tác bạn muốn thực hiện (1-10): "))
    return choice

def create_list(N):
    user_lst = []
    for _ in range(N):
        user_lst.append(random.randint(1,100))
    return user_lst

def find_max(user_lst):
    max = 0
    index_lst = []
    for _ in range(len(user_lst)):
        if user_lst[_] >= max:
            max = user_lst[_]
            index_lst.append(_) 

    index_lst = sorted(index_lst)
    max_idx = index_lst[-1]
    print(f"Số lớn nhất trong mảng là: {max}")
    print(f"Vị trí cuối cùng của số lớn nhất: {max_idx}")

def count_equal_X(user_lst):
    X = int(input("Nhập số X bạn muốn đếm (1-100): "))
    count = 0
    index_lst = []
    for _ in range(len(user_lst)):
        if user_lst[_] == X:
            count += 1
            index_lst.append(_)

    print(f"Số lần xuất hiện của {X} trong mảng là: {count}")
    print(f"Các vị trí xuất hiện là: {index_lst}")

def print_element_index(user_lst):
    pass

def find_no_coincident(user_lst):
    pass

def find_coincident_index(user_lst):
    pass

def find_decreasing_subarrays(user_lst):
    pass

def user_controller(user_lst, choice):
    while choice > 0 and choice <= 10:
        if choice == 1:
            print(f"{user_lst}\n")
            choice = menu()
        elif choice == 2:
            print(f"{user_lst[::-1]}\n")
            choice = menu()
        elif choice == 3:
            print(f"{sorted(user_lst)}\n")
            choice = menu()
        elif choice == 4:
            find_max(user_lst)
            print()
            choice = menu()
        elif choice == 5:
            count_equal_X(user_lst)
            print()
            choice = menu()
        elif choice == 6:
            print_element_index(user_lst)
            print()
            choice = menu()
        elif choice == 7:
            find_no_coincident(user_lst)
            print()
            choice = menu()
        elif choice == 8:
            find_coincident_index(user_lst)
            print()
            choice = menu()
        elif choice == 9:
            find_decreasing_subarrays(user_lst)
            print()
            choice = menu()
        elif choice == 10:
            print("Cảm ơn bạn đã dùng")
            break

def main():
    N = int(input("Nhập độ dài của danh sách bạn muốn khởi tạo: "))
    lst = create_list(N)
    choice = menu()
    user_controller(lst, choice)

main()