import requests
import pandas as pd
import json
import logging
from pathlib import Path
from datetime import datetime

# -----------------------------
# Настройка логирования
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# -----------------------------
# Константы
# -----------------------------
API_URL = "https://open.er-api.com/v6/latest/USD"

# Папка для сохранения результатов
OUTPUT_DIR = Path.home() / "currency_rates_output"
OUTPUT_DIR.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

JSON_BACKUP_FILE = OUTPUT_DIR / f"rates_backup_{timestamp}.json"
CSV_FILE = OUTPUT_DIR / f"currency_rates_{timestamp}.csv"
XLSX_FILE = OUTPUT_DIR / f"currency_rates_{timestamp}.xlsx"


# -----------------------------
# Получение данных с API
# -----------------------------
try:
    logging.info("Отправка запроса к API...")

    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()

    logging.info("Данные успешно получены")

except requests.RequestException as e:
    logging.error(f"Ошибка при запросе к API: {e}")
    raise SystemExit(1)

# -----------------------------
# Бекап JSON
# -----------------------------
try:
    with open(JSON_BACKUP_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    logging.info(f"JSON backup сохранен: {JSON_BACKUP_FILE}")

except Exception as e:
    logging.error(f"Ошибка при сохранении JSON backup: {e}")

# -----------------------------
# Парсинг в DataFrame
# -----------------------------
try:
    rates = data.get("rates", {})

    df = pd.DataFrame(
        rates.items(),
        columns=["Currency", "Rate_to_USD"]
    )

    logging.info("DataFrame успешно создан")

except Exception as e:
    logging.error(f"Ошибка при создании DataFrame: {e}")
    raise SystemExit(1)

# -----------------------------
# Сохранение CSV
# -----------------------------
try:
    df.to_csv(CSV_FILE, index=False)

    logging.info(f"CSV файл сохранен: {CSV_FILE}")

except Exception as e:
    logging.error(f"Ошибка при сохранении CSV: {e}")

# -----------------------------
# Сохранение XLSX
# -----------------------------
try:
    df.to_excel(XLSX_FILE, index=False)

    logging.info(f"XLSX файл сохранен: {XLSX_FILE}")

except Exception as e:
    logging.error(f"Ошибка при сохранении XLSX: {e}")

logging.info("Скрипт завершил работу")
