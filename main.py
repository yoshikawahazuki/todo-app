import json

try :
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []

while True:
    print("\n1:追加 2:一覧 3:削除 4:終了")
    choice = input("選択してください： ")

    if choice == "1":
        task = input("タスクを入力してください： ")
        tasks.append(task)

        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
    
    elif choice == "2":
        print("=== タスク一覧 ===")
        for i , t in enumerate(tasks):
            print(f"{i}: {t}")

    elif choice == "3":
        print("=== タスク一覧 ===")
        for i , t in enumerate(tasks):
            print(f"{i}: {t}")

        num = int(input("削除する番号を入力してください： "))
        tasks.pop(num)

        with open("tasks.json", "w") as f:
            json.dump(tasks, f)

        print("削除しました")
    
    elif choice == "4":
        print("終了します")
        break
    
    else:
        print("無効な入力です")