tasks = []

while True:
    print("\n1:追加 2:一覧 3:終了")
    choice = input("選択してください： ")

    if choice == "1":
        task = input("タスクを入力してください： ")
        tasks.append(task)
    
    elif choice == "2":
        print("=== タスク一覧 ===")
        for i , t in enumerate(tasks):
            print(f"{i}: {t}")
    
    elif choice == "3":
        print("終了します")
        break
    
    else:
        print("無効な入力です")