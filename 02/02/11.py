letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
text = input() + ' запретил букву'
for i in letters:
    if i in text:
        print(text, i)
        text = ''.join(text.split(i)).strip()
        text = ' '.join(text.split()).strip()
