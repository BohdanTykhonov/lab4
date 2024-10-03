# Тихонов Богдан: Текст, який будемо обробляти
text = "  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.  "

# 1. Тихонов Богдан: Використовуємо функцію strip() для видалення зайвих пробілів на початку та в кінці рядка
clean_text = text.strip()

# 2. Тихонов Богдан: Використовуємо функцію lower() для переведення всього тексту в нижній регістр
lower_case_text = clean_text.lower()

# 3. Тихонов Богдан: Використовуємо функцію replace() для заміни "dolor" на "Python"
replaced_text = lower_case_text.replace("dolor", "Python")

# 4. Ткаченко Ілля: Використовуємо функцію splitlines() для розбиття тексту на рядки
split_text = replaced_text.splitlines()

# 5. Ткаченко Ілля: Використовуємо функцію join() для об'єднання рядків у текст з пробілами
joined_text = " ".join(split_text)

# 6. Ткаченко Ілля: Використовуємо функцію title() для перетворення кожного слова на текст із великої літери
final_text = joined_text.title()

# Виводимо кінцевий результат
print(final_text)