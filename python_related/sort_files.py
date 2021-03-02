import os
import shutil
import time


def get_file(path_original):
    paths = {}
    for root, dirs, files in os.walk(path_original):
        for file in files:
            full_path = os.path.join(root, file)
            modify_time = time.strftime('%Y-%m', time.localtime(os.stat(full_path).st_mtime))
            paths[full_path] = modify_time
    return paths


def move_org(path):
    f_path, f_name = os.path.split(path[0])
    folder_name = path[1]
    des_path = os.path.join(f_path, folder_name)

    if os.path.exists(des_path):
        shutil.move(path[0], des_path)
    else:
        os.mkdir(des_path)
        shutil.move(path[0], des_path)


def main():
    path_original = r"D:\Image"
    paths = get_file(path_original)
    for path in paths.items():
        move_org(path)
