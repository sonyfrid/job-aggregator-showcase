# 🤖 IT Job Aggregator Bot

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-45ba4b?style=for-the-badge&logo=playwright)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite)

<div align="center">
  <h3>Автоматический агрегатор IT-вакансий с умной фильтрацией</h3>
</div>

---

## 💡 Зачем нужен этот бот

Поиск работы в IT — это рутина: десятки каналов, мусор, пропущенные вакансии. Бот автоматизирует всё:

- **Читает 30+ источников** — Telegram, job-борды
- **Фильтрует по стеку**
- **Убирает мусор** 
- **Присылает только релевантное** — в удобный Telegram-канал

**Результат:** 2-3 часа рутины → 5 минут просмотра.

---

## 🎯 Сложности
На первый взгляд кажется: «Ну, парсинг, фильтр — что тут сложного?»

На самом деле:

- **Источники разные** — Telegram-каналы, сайты, API. У каждого своя структура.
- **Данные грязные** — вакансии дублируются, содержат мусор, рекламу, подборки.
- **Фильтры неочевидны** — у каждых вакансий своя структура. Например, «удалёнка» пишется 10 способами 
- **Лимиты и защита** — источники не любят автоматизацию. Нужны паузы, ротация.
- **Надёжность** — бот работает 24/7, не падает, не шлёт дубли, не теряет данные.

**Это компактный продукт с архитектурой, базой данных, логированием и тестами.**

---

## 🏗️ Архитектура

```mermaid
flowchart LR
    subgraph INPUT["📥 Сбор"]
        direction TB
        TG[Telegram-каналы]
        JB[Job-борды]
    end
    
    subgraph PROCESS["⚙️ Обработка"]
        direction TB
        P1[Парсер]
        P2[Фильтр]
        P3[Дедупликация]
    end
    
    subgraph DATA["💾 Данные"]
        DB[(SQLite)]
    end
    
    subgraph OUTPUT["📤 Результат"]
        CH[Telegram-канал]
    end
    
    TG --> P1
    JB --> P1
    P1 --> P2 --> P3
    P3 --> DB --> CH
```

---

## 📸 Демонстрация

### Терминал

<table>
  <tr>
    <td align="center">
      <img src="screenshots/terminal.png" width="400"><br>
      <b>На страже стоят автотесты</b>
    </td>
    <td align="center">
      <img src="screenshots/terminal1.png" width="400"><br>
      <b>Запуск бота с инфо</b>
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
      <b></b>
    </td>
    <td align="center">
      <img src="screenshots/channel2.png" width="250"><br>
      <b></b>
    </td>
  </tr>
</table>

---

## 📊 Результаты

| Метрика | Значение |
|---------|----------|
| Источников | 30+ |
| Отфильтрованных вакансий в день | 50 |
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
