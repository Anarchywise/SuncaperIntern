import os
import shutil

# 获取当前脚本所在的目录
script_directory = os.path.dirname(os.path.abspath(__file__))

# 切换到目标目录
os.chdir(script_directory)


# 文件读取示例
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:  # with 会自动关闭文件
            content = file.read()
            print(f"Content of {file_path}:\n{content}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# 文件写入示例
def write_file(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
            print(f"Content successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# 文件追加示例
def append_to_file(file_path, content):
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(content)
            print(f"Content successfully appended to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# 文件复制示例
def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f"File copied from {source_path} to {destination_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# 文件移动示例
def move_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"File moved from {source_path} to {destination_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# 文件删除示例
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File deleted: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# 主程序
if __name__ == "__main__":
    # 读取文件
    read_file("example.txt")

    # 写入文件
    new_content = "This is a new content for the file."
    write_file("example_new.txt", new_content)

    # 追加到文件
    append_content = "\nThis is additional content."
    append_to_file("example_new.txt", append_content)

    # 复制文件
    copy_file("example_new.txt", "example_copy.txt")

    # # 移动文件
    # move_file('example_copy.txt', 'backup/example_copy.txt')

    # # 删除文件
    # delete_file('example_copy.txt')
