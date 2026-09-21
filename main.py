def classify_message(message):
    text = message.lower()

    complaint_words = [
        "очередь",
        "холодная",
        "пропал",
        "не работает",
        "проблема",
    ]

    information_words = [
        "как получить",
        "справка",
        "где парковка",
        "где находится",
    ]

    if any(word in text for word in complaint_words):
        return "жалоба"

    if any(word in text for word in information_words):
        return "справка"

    return "другое"


def generate_answer(category):
    answers = {
        "справка": (
            "Здравствуйте! Спасибо за обращение. "
            "Мы уточним необходимую информацию и подскажем, как получить нужные сведения."
        ),
        "жалоба": (
            "Здравствуйте! Спасибо, что сообщили о проблеме. "
            "Мы передадим информацию ответственным сотрудникам для проверки."
        ),
        "другое": (
            "Здравствуйте! Спасибо за обращение. "
            "Мы рассмотрим ваш запрос и предоставим информацию в ближайшее время."
        ),
    }
    return answers[category]


with open("messages.txt", "r", encoding="utf-8") as file:
    messages = [line.strip() for line in file if line.strip()]


for i, message in enumerate(messages, start=1):
    category = classify_message(message)
    answer = generate_answer(category)

    print(f"Обращение {i}: {message}")
    print(f"Категория: {category}")
    print(f"Черновик ответа: {answer}")
    print("-" * 70)
