# Currency Rates Parser

Скрипт получает курсы валют к USD через открытое API,
сохраняет backup ответа в JSON,
а также экспортирует данные в CSV и XLSX.

## Что делает скрипт

- Получает курсы валют к USD
- Делает backup JSON-ответа
- Создает pandas.DataFrame
- Сохраняет:
  - CSV
  - XLSX
- Пишет базовые логи

## Установка

Установить зависимости:

```bash
pip install pandas requests openpyxl
