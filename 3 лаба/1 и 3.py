def open_read_file(file_name, type_of_reading):
    if type_of_reading == '1':
        with open(f'{file_name}', 'r') as file:
            content = file.read()
            print(content)

    elif type_of_reading == '2':
        with open(f'{file_name}', 'r') as file:
            for line in file:
                print(line)

input_file_name = input('введите имя файла, который вы хотите открыть\n')  #существующий файл: 'example.txt'
input_type_of_reading = input('введите "1", чтобы выбрать чтение всего файла\nвведите "2", чтобы выбрать построчное '
                              'чтение файла\n')



try:
    open_read_file(input_file_name, input_type_of_reading)
except FileNotFoundError:
    print('файла с таким именем не найдено')

