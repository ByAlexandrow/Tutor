import json
import os


SOURCE_JSON = 'all_reviews.json'
FIXTURE_FILE = '../fixture/reviews_result.json'

os.makedirs(os.path.dirname(FIXTURE_FILE), exist_ok=True)  # Создаем папку fixtures если её нет

# Читаем исходный json-файл с данными
with open(SOURCE_JSON, 'r', encoding='utf-8') as f:
    original_data = json.load(f)

print(f"Прочитано {len(original_data)} записей из {SOURCE_JSON}")

# Маппинг месяцев для преобразования даты
MONTHS = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12'
}

# Формируем фикстуру
fixture_data = []
pk_counter = 1

for item in original_data:
    date_str = item['date']  # Парсим дату
    parts = date_str.split()  # Делим ее на части
    day = parts[0].zfill(2)  # Берем день
    month_ru = parts[1].lower()  # Берем месяц в виде строки
    year = parts[2]  # Берем год
    month_num = MONTHS.get(month_ru)  # Преобразуем месяц в числовой формат
    db_date = f"{year}-{month_num}-{day}"  # Сохраняем в виде гггг-мм-дд для БД
    
    # Создаем запись фикстуры
    fixture_record = {
        "model": "reviews.review",  # Указываем имя приложения и имя модели для вставки данных (app_name.model_name)
        "pk": pk_counter,  # Указываем id для каждой записи, автоматическая подстановка (primary key)
        "fields": {
            "name": item['name'],
            "star": float(item['star']),
            "aim": item['aim'][:150],  # Приводим к модельным ограничениям (обрезаем до 150 символов)
            "review": item['review'],
            "date": db_date,
            "is_published": True
        }
    }
    
    fixture_data.append(fixture_record)  # Добавляем запись в список фикстуры
    pk_counter += 1  # Увеличиваем id каждой записи

# Сохраняем фикстуру
with open(FIXTURE_FILE, 'w', encoding='utf-8') as f:
    json.dump(fixture_data, f, ensure_ascii=False, indent=2)

# Логи отладки
print(f"Создана фикстура: {FIXTURE_FILE}")
print(f"Сохранено записей: {len(fixture_data)}")

# print("\nПример записи фикстуры:")
# print(json.dumps(fixture_data[0], ensure_ascii=False, indent=2))
