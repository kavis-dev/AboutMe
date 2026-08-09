import os
#Init
todo_list = []
saved = False
#Read
def read_save(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                todo_list.append(line.strip())
    except FileNotFoundError:
        print("儲存檔案不存在")
        return "FileNotFound"
#Add
def add():
    todo = input("輸入要新增的事項：")
    todo_list.append(todo)
    print(f"已新增 Todo 事項：{todo}")
    global saved
    saved = False
#Show
def show():
    for num, todo in enumerate(todo_list, start=1):
        print(f"{num}. {todo}")
    print(f"共有 {len(todo_list)} 項Todo")
#Delete
def delete():
    show()
    try:
        del_num = int(input("請輸入你要刪除的事項編號：")) - 1
    except ValueError:
        print("請輸入數字")
        return
    if 0 <= del_num < len(todo_list):
        print(f"已刪除事項：{todo_list.pop(del_num)}")
        saved = False
    else:
        print("輸入的編號不存在")
#Save
def save():
    with open("todo_list.txt", "w", encoding="utf-8") as f:
        for num, todo in enumerate(todo_list, start=1):
            f.write(f"{todo}\n")
    global saved
    saved = True
#Main
def main():
    print("==== Todo ====\n1. 新增事項\n2. 查看事項\n3. 刪除事項\n4. 儲存\n5. 退出\n")
    user_input = input("要讀取儲存的 Todo List 嗎？(y/n)：")
    if user_input.lower() == "y":
        user_input = input("輸入要讀取的檔案名稱：")
        if read_save(user_input) == "FileNotFound":
            print("找不到檔案")
        else:
            print(f"已讀取儲存在 {user_input} 中的 {len(todo_list)} 個 Todo 事項")
    while True:
        user_input = input("> ")
        if user_input == "1":
            add()
        elif user_input == "2":
            show()
        elif user_input == "3":
            delete()
        elif user_input == "4":
            save()
        elif user_input == "5":
            if saved:
                break
            else:
                user_input = input("尚未儲存 Todo List，確定要退出嗎?(y：直接退出 n：不要退出 s：儲存並退出)：")
                if user_input.lower() == "y":
                    break
                elif user_input.lower() == "n":
                    continue
                elif user_input.lower() == "s":
                    save()
                    break
        elif user_input == "clear":
            os.system("cls")
            print("==== Todo ====\n1. 新增事項\n2. 查看事項\n3. 刪除事項\n4. 離開\n5. 儲存\n")
        else:
            print("請輸入有效功能編號")
if __name__ == "__main__":
    main()