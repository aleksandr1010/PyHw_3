dict = {
1: "А, В, Е, И, Н, О, Р, С, Т",
2: "Д, К, Л, М, П, У ",
3: "Б, Г, Ё, Ь, Я",
4: "Й, Ы",
5: "Ж, З, Х, Ц, Ч" ,
8: "Ш, Э, Ю ",
10: "Ф, Щ, Ъ",
}
n = input('Введите слово  ').upper()

print(f'Вы получаете: {sum([key for letter in n for key, value in dict.items() if letter in value])} очков')