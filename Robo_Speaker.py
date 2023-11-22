import os

if __name__ == '__main__':
    while True:
        x = input("Enter the string you want to pronounce")
        if x == "wq":
            break
        command = f"say{x}" #* Operational for MacOS
        os.system(command=command)