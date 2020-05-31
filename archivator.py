import os
import time
import zipfile


def main():
    # 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
    #source = ['C:\\Users\\Владюша\\Documents ']
    # список дирректорий для архивации у меня linux поэтому другой формат
    source = ['./Documents/test/', './Documents/test1/', './Documents/test0/']
    # 2. Резервные копии должны храниться в основном каталоге резерва.
    #target_dir = 'C:\\Users\\Владюша\\Desktop\\ Резерв'
    target_dir = 'Documents/reserv_folder'
    # 3. Файлы помещаются в zip-архив
    # 4. Текущая дата служит именем для подкаталога в основном каталоге.
    today = target_dir + os.sep + time.strftime('%Y%m%d')

    # 4.1. Текущее время служит именем zip-архива.
    now = time.strftime('%H%M%S')

    # 4.2. Запрашиваем комментарий пользователя для имени файла.
    comment = input("Введите комментарий: ")
    if len(comment) == 0:  # Проверяем, введен ли комментарий.
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + '_' + comment.replace(' ', '_') + ".zip"

    # 4.3. Создаем каталог, если его еще нет.
    if not os.path.exists(today):
        os.mkdir(today)  # Создание каталога.
    print("Каталог {} успешно создан.".format(today))

    # получаем список файлов для архивации
    for item in source:
        for root, dirs, files in os.walk(item):
            print(files)
            # создаём архив и добавляем файлы
            with zipfile.ZipFile(target, 'a') as myzip:
                for file in files:
                    myzip.write(os.path.join(root, file))


if __name__ == "__main__":
    main()