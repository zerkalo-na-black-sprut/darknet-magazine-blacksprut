from datetime import datetime

def days_until_vacation(vacation_date_str="2025-07-01"):
    today = datetime.today()
    vacation = datetime.strptime(vacation_date_str, "%Y-%m-%d")
    delta = vacation - today
    if delta.days < 0:
        print("Отпуск уже был! Пора планировать следующий 🌴")
    else:
        print(f"До отпуска осталось {delta.days} дней. Терпи! 🧳")

days_until_vacation()  # Подставь свою дату!
