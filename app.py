import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"{filename} created successfully!")
    except FileExistsError:
        print(f"{filename} already exists!")  
    except Exception:
        print("An error occurred!")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found")
    else:
        print("Files in directory")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} deleted successfully!")
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("An error occurred!")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of {filename}: \n{content}")
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("An error occurred!")

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
                  content = input("Enter data to add: ")
                  f.write(content + "\n")
                  print(f'Content added to {filename} success')                   
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("An error occurred!")

def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1. Create file')
        print('2. View all files')
        print('3. Delete file')
        print('4. Read file')
        print('5. Edit file')
        print('6. Exit')

        choice = input("Enter action (1-6): ")

        if choice == '1':
            filename = input("Enter the filename you want to create: ")
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter the filename you want to delete: ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the filename you want to read: ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the filename you want to edit: ")
            edit_file(filename)
        elif choice == '6':
            print("App Closed")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()