from fastapi import FastAPI
from datetime import date
import uvicorn

#Создаем объект приложения
app = FastAPI()

#Определяем маршрут (эндпоинт)
@app.get("/info")
async def get_days_to_new_year():
    # 1. Получаем текущую дату
    today = date.today()

#Вычисляем дату следующего Нового года
    next_year = today.year + 1
    new_year_date = date(next_year, 1, 1)

#Находим разницу
    delta = new_year_date - today

#Возвращаем результат
    return {
        "days_before_new_year": delta.days
    }

#Точка входа в программу
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=4200)