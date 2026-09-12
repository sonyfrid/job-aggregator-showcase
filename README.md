# 🤖 IT Job Aggregator Bot

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-45ba4b?style=for-the-badge&logo=playwright)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite)

<div align="center">
  <h3>Автоматический агрегатор IT-вакансий с умной фильтрацией</h3>
</div>

---

## 📋 О проекте

Бот собирает IT-вакансии из 30+ источников, фильтрует по стеку и отправляет только релевантные в Telegram.

**Что умеет:**
- 🧠 Сбор вакансий из множества источников
- 🧠 Умная фильтрация (Playwright, TypeScript, Python, QA)
- 🧠 Сохранение в SQLite
- 🧠 Отправка в Telegram канал
- 🧠 Защита от дубликатов
- 🧠 Лимиты и паузы

---
## 📁 Структура проекта

```mermaid
flowchart TD
    A[job-aggregator] --> B[src/]
    A --> C[tests/]
    A --> D[screenshots/]
    A --> E[README.md]
    A --> F[LICENSE]
    
    B --> B1[core/]
    B --> B2[filters/]
    B --> B3[storage/]
    B --> B4[handlers/]
    
    B1 --> B11[config.py]
    B1 --> B12[client.py]
    
    B2 --> B21[keyword_filter.py]
    B2 --> B22[date_filter.py]
    
    B3 --> B31[database.py]
    B3 --> B32[models.py]
    
    B4 --> B41[message_handler.py]
    B4 --> B42[hh_parser.py]
    
    C --> C1[test_filters.py]
    C --> C2[test_database.py]
    C --> C3[test_api.py]
```
## 🏗️ Архитектура

```mermaid
flowchart LR
    A[Источники] --> B[Фильтры]
    B --> C[SQLite]
    C --> D[Telegram]
```

---

## 📸 Демонстрация

### Терминал
<table>
  <tr>
    <td align="center">
      <img src="screenshots/terminal.png" width="400"><br>
      <b>Запуск бота</b>
    </td>
    <td align="center">
      <img src="screenshots/terminal1.png" width="400"><br>
      <b>Обработка вакансий</b>
    </td>
  </tr>
</table>

### Telegram-канал
<table>
  <tr>
    <td align="center">
      <img src="screenshots/channel.png" width="250"><br>
      <b>Вакансии QA</b>
    </td>
    <td align="center">
      <img src="screenshots/channel1.png" width="250"><br>
      <b>Фильтрация</b>
    </td>
    <td align="center">
      <img src="screenshots/channel2.png" width="250"><br>
      <b>Отправка</b>
    </td>
  </tr>
</table>
---

## 📊 Результаты

| Метрика | Значение |
|---------|----------|
| Источников | 30+ |
| Вакансий в день | 50 |
| Релевантность | 95% |
| Ручной работы | 0 |

---

## 🛠️ Стек

- Python 3.13
- Playwright
- SQLite
- asyncio
- pytest

---

## ⚠️ Исходный код

Исходный код находится в **приватном репозитории**.

Демонстрация доступна на собеседовании или по запросу.

**Контакт:** [Telegram](https://t.me/fridmo_sony)

---

## 👨‍💻 Автор

**Sony Fridmo** — QA Automation Engineer

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram)](https://t.me/fridmo_sony)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github)](https://github.com/sonyfrid)

---

<div align="center">
  <sub>Built with ❤️ by QA Automation Engineer</sub>
</div>
