import sys
import os

def demo_sys_module():
    # sys.argv: command-line arguments
    print("Command line args:")
    for index, arg in enumerate(sys.argv):
        print(f"Argument {index}: {arg}")
    print(sys.argv, type(sys.argv))

    # sys.path
    print("\n\nPaths:")
    sys.path.append(r"c:\Ramakant\Test\Folder\bin")
    for index, path in enumerate(sys.path):
        print(f"Argument {index}: {path}")

    # sys.version
    print(f"{sys.version = }")


def demo_os_module():
    current_dir = os.getcwd()
    print(f"Current working Directory: {current_dir}")

    # Create a new directory
    new_dir = os.path.join(current_dir, 'demo_dir')
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print(f"\nDirectory 'demo_dir' created at {new_dir}")
    else:
        print(f"\nDirectory 'demo_dir' already exists at {new_dir}")

    # List the files and directories in the cwd
    print("\nFiles and directories in the current directory:")
    for item in os.listdir(current_dir):
        print(f"\t{item}")

    # Create a new file in the new directory
    new_file_path = os.path.join(new_dir, "demo_file.txt")

    # Version 1
    # file = open(new_file_path, 'w')
    # file.write("This is a demo file.\n")
    # file.flush()
    # file.write("Some more info.")
    # file.close()

    # Version 2 (With try-except block)
    # try:
    #     file = open(new_file_path, 'w')
    #     file.write("This is a demo file.\n")
    #     file.flush()
    #     file.write("Some more info.")
    # except FileNotFoundError as e:
    #     print(f"{e!r}")
    # except Exception as e:
    #     print(f"{e!r}")
    # finally:
    #     if file:
    #         file.close()

    # Version 3 (Context manager  -- 'with' block)
    lines = ["Third line\n", "Fourth line\n", "Fifth line\n"]
    with open(new_file_path, 'w') as file:
        file.write("This is a demo file.\n")
        file.flush()
        file.write("Some more info.\n")
        file.writelines(lines)
        # file.close() # Note require here anymore
        

    # Read from the file
    with open(new_file_path, 'r') as file:
        read_data = file.read(10)
        print(read_data)

        read_data = file.readline()
        print(read_data)

        read_data = file.readlines()
        print(read_data)


    # Check if file exists
    if os.path.exists(new_file_path):
        print(f"\nFile 'demo_file.txt' exists at {new_file_path}.")

    # Remove the file
    os.remove(new_file_path)
    print(f"\nFile 'demo_file.txt' removed from {new_file_path}.")

    # Remove the directory
    os.rmdir(new_dir)
    print(f"\nDirectory 'demo_dir' removed from {new_dir}")

# demo_sys_module()
demo_os_module()
