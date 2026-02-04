import json
import re


def reviews_txt_to_json_simple(input_file='reviews.txt', output_file='reviews.json'):
    """
    Чтение txt-файла с отзывами и его перевод в json.
    Структура файла с отзывами: имя, дата, предмет, текст откзыва.
    """

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    raw_reviews = content.split('\n\n')  # Разделяем отзывы по двойным переносам строк (предполагаем такой формат)

    reviews_list = []
    
    for review_block in raw_reviews:  
        lines = review_block.strip().split('\n')
        
        if len(lines) >= 4:  # Должно быть минимум 4 строки: имя, дата, предмет, текст
            name = lines[0].strip()
            date = lines[1].strip()
            subject = lines[2].strip()
            
            # Текст отзыва может быть на нескольких строках
            text_lines = lines[3:]
            text = '\n'.join(text_lines).strip()
            
            reviews_list.append({
                'name': name,
                'star': 5,
                'date': date,
                'subject': subject,
                'text': text
            })
    
    # Сохраняем в JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(reviews_list, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Готово! Создан файл: {output_file}")
    print(f"📊 Обработано отзывов: {len(reviews_list)}")
    
    return reviews_list


if __name__ == "__main__":
    reviews_txt_to_json_simple('reviews.txt', 'reviews.json')
