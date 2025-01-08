uzer_text_input = input('введите ваш текст:\n')
with open('user_input.txt', 'w') as file:
    file.write(uzer_text_input)


possible_to_adding = input('введите текст, который хотите добавить,\nесли добавить нечего введите "2"\n')
while '2' not in possible_to_adding:
    with open('user_input.txt', 'a') as file:
        file.write(possible_to_adding)
    possible_to_adding = input('введите текст, который хотите добавить,\nесли добавить нечего введите "2"\n')


