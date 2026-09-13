<div align="center">

<img src="screenshots/botvacancy.png.png" width="150" alt="Logo">

# IT Job Aggregator Bot

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=3000&color=45BA4B&center=true&vCenter=true&lines=Автоматический+сбор+вакансий;Умная+фильтрация;Работает+24%2F7">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-45ba4b?style=for-the-badge&logo=playwright)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

---

## 💡 Зачем нужен этот бот

Поиск работы в IT — это рутина: десятки каналов, мусор, пропущенные вакансии. Бот найдет и автоматизиурет всё за вас:

- **Читает 30+ источников** — Telegram, job-борды
- **Фильтрует по стеку**
- **Убирает мусор** — неактуальную информацию
- **Присылает только релевантное** — в приватный индивидуальный Telegram-канал

**Результат:** 2-3 часа рутины → 5 минут просмотра.

---

## 🎯 Специфика

<details>
<summary>🔍 Нажми, чтобы раскрыть</summary>

На первый взгляд кажется: «Ну, парсинг, фильтр — что тут сложного?»

На самом деле:

- **Источники разные** — Telegram-каналы, сайты, API. У каждого своя структура.
- **Данные грязные** — вакансии дублируются, содержат мусор, рекламу, подборки.
- **Фильтры неочевидны** — у каждых вакансий своя структура. Например, «удалёнка» пишется 10 способами.
- **Лимиты и защита** — источники не любят автоматизацию. Нужны паузы, ротация.
- **Надёжность** — бот работает 24/7, не падает, не шлёт дубли, не теряет данные.

**Это компактный продукт с архитектурой, базой данных, логированием и тестами.**

</details>

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

### 🖥️ Терминал

<table>
  <tr>
    <td align="center">
      <img src="screenshots/terminal.png" width="400"><br>
      <b>🛡️ На страже автотесты</b>
    </td>
    <td align="center">
      <img src="screenshots/terminal1.png" width="400"><br>
      <b>🚀 Запуск бота с инфо</b>
    </td>
  </tr>
</table>

### 📱 Telegram-канал

<table>
  <tr>
    <td align="center">
      <img src="screenshots/channel.png" width="250"><br>
      <b>💼 Вакансии QA</b>
    </td>
    <td align="center">
      <img src="screenshots/channel1.png" width="250"><br>
      <b>🎯 Вакансии</b>
    </td>
    <td align="center">
      <img src="screenshots/channel2.png" width="250"><br>
      <b>📤 Вакансии</b>
    </td>
  </tr>
</table>

---

## 📊 Результаты

<div align="center">

| 📈 Метрика | 🎯 Значение |
|:----------:|:-----------:|
| **Источников** | 30+ |
| **Вакансий в день** | 50 |
| **Релевантность** | 95% |
| **Ручной работы** | 0 |

</div>

---

## 🛠️ Стек

<div align="center">

<br><br>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-45ba4b?style=flat-square&logo=playwright&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![asyncio](https://img.shields.io/badge/asyncio-3776AB?style=flat-square&logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)

</div>

---

## 🗺️ Roadmap

- [x] Сбор из Telegram
- [x] Сбор с job-бордов
- [x] Умная фильтрация
- [x] Сохранение в SQLite
- [x] Защита от дубликатов
- [x] Автотесты

---

<div align="center">

## **Нужен похожий бот для ваших задач?**

Напишите мне - обсудим любые идеи:
</div>

<div align="center">

**Sony Fridmo** — QA Automation Engineer

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/fridmo_sony)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sonyfrid)

</div>

---
## ⚠️ Исходный код

Исходный код находится в **приватном репозитории**.

Демонстрация доступна по запросу.

---
<div align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">
  <br>
  <sub>Built with ❤️ by QA Automation Engineer</sub>
</div>
