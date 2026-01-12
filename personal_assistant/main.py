def main():
    print("Персональний помічник запущено!")
    while True:
        command = input(">>> ")
        if command.lower() in ("exit", "quit"):
            print("До побачення!")
            break
        print(f"Ви ввели: {command}")
