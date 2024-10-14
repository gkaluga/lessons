import os
import datetime


def get_dir_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.realpath(root)
            filepath = os.path.join(path, file)
            filesize = os.path.getsize(filepath)
            fmtimestamp = int(os.path.getmtime(filepath))
            fmdt = datetime.datetime.fromtimestamp(fmtimestamp)
            parent_dir = os.path.dirname(path)
            print(
                f'Обнаружен файл: {file}, Путь: {path}, Размер: {filesize} байт, ' +
                f'Время изменения: {fmdt:%d.%m.%Y %H:%M:%S}, Родительская директория: {parent_dir}')


directory = '.'
get_dir_files(directory)
