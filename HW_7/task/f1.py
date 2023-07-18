# 1 — Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extension>


from pathlib import Path


def rename_files(path, old_ext, new_ext, new_name):
    directory = Path(path)
    files_to_rename = [i for i in directory.iterdir() if i.suffix == f'.{old_ext}']
    for k, file in enumerate(files_to_rename, start=1):
        file.rename(f'{file.stem}_{new_name}_{k}.{new_ext}')


if __name__ == '__main__':
    rename_files('..', 'txt', 'png', 'file')
