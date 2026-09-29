<div align="center">

<img src="screenshots/buff_cat_green3.png" width="100" alt="HunterKitty Work">

# HunterKitty Work

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=3000&color=00FF32&center=true&vCenter=true&lines=Откликайся+первым+на+вакансии;Telegram-бот+%2B+Mini+App;16+сайтов+%2B+169+Telegram-каналов">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![aiogram](https://img.shields.io/badge/aiogram-3-2CA5E0?style=for-the-badge&logo=telegram)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Tests](https://img.shields.io/badge/tests-292_passed-brightgreen?style=for-the-badge&logo=pytest)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

---

## 💡 Что это

На вакансию откликаются в первые часы — кто раньше, у того шанс выше. HunterKitty Work собирает свежие вакансии со всех площадок в одну ленту и присылает новые сразу, как их опубликовали.

- **16 сайтов и 169 Telegram-каналов** сайты и каналы читаются в реальном времени
- **3000+ новых вакансий в день** — дубли, реклама, резюме и мошенники отсеиваются
- **Точный подбор** — профессия, ключевые слова, слова-исключения, город, формат работы
- **✉️ Письмо работодателю** — ИИ составляет сопроводительное под конкретную вакансию
- **Telegram-бот и Mini App** — лента, сохранённые, уведомления «сразу / раз в час / раз в день»

---

## 📸 Mini App

Терминал в стиле 2000-х: две темы, три размера текста.

<table>
  <tr>
    <td align="center"><img src="screenshots/app-search-dark.png" width="250"><br><b>🔎 Поиск</b></td>
    <td align="center"><img src="screenshots/app-feed.png" width="250"><br><b>📜 Лента</b></td>
    <td align="center"><img src="screenshots/app-vacancy.png" width="250"><br><b>💼 Вакансия и письмо</b></td>
  </tr>
  <tr>
    <td align="center"><img src="screenshots/app-search-light.png" width="250"><br><b>☀️ Светлая тема</b></td>
    <td align="center"><img src="screenshots/app-about.png" width="250"><br><b>✍️ О себе и настройки</b></td>
  </tr>
</table>

### 🖥️ Терминал

<table>
  <tr>
    <td align="center">
      <img src="screenshots/terminal.png" width="400"><br>
      <b>🛡️ На страже автотесты</b>
    </td>
    <td align="center">
      <img src="screenshots/terminal4.png" width="400"><br>
      <b>🚀 Запуск бота с инфо</b>
    </td>
  </tr>
</table>

---

## 🎯 Что внутри

<details>
<summary>🔍 Нажми, чтобы раскрыть</summary>

- **Нормализация** — зарплата, город, формат работы («удалёнка» пишется десятком способов), опыт, дедупликация одной вакансии с разных площадок.
- **Подбор** — синонимы профессий и «родственные» роли, конфликт ролей и стеков, жёсткие фильтры и ранжирование, «умные» ключевые слова.
- **Уведомления** — сразу, пачкой или утренней подборкой; ничего не теряется.
- **Mini App** — aiohttp + PYTHON и JS внутри процесса бота.
- **Подписка** — пробный период, бесплатный режим с лимитами и PRO с оплатой через ЮKassa.
- **Надёжность** — воркер отдельно от бота (кнопки не подвисают), расчёт подбора в отдельных процессах, ночные бэкапы базы, 292 автотеста.

</details>

---

## 🏗️ Архитектура

```mermaid
flowchart LR
    subgraph INPUT["📥 Сбор"]
        direction TB
        SITES[16 сайтов]
        TG[169 Telegram-каналов]
    end

    subgraph PROCESS["⚙️ Обработка"]
        direction TB
        N[Нормализация]
        D[Дедупликация]
        M[Подбор под человека]
    end

    subgraph DATA["💾 Данные"]
        DB[(PostgreSQL)]
    end

    subgraph OUTPUT["📤 Результат"]
        direction TB
        BOT[Telegram-бот]
        APP[Mini App]
        AI[✉️ ИИ-письмо]
    end

    SITES --> N
    TG --> N
    N --> D --> DB --> M
    M --> BOT
    M --> APP
    APP --> AI
```

---

## 📊 Цифры

<div align="center">

| 📈 Метрика | 🎯 Значение |
|:----------:|:-----------:|
| **Сайтов** | 16 |
| **Telegram-каналов** | 169 |
| **Новых вакансий в день** | 3000+ |
| **Автотестов** | 292 |

</div>

---

## 🛠️ Стек

<div align="center">

<br>

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="70" title="Python">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="70" title="PostgreSQL">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" width="70" title="SQLAlchemy">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="70" title="JavaScript">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg" width="70" title="pytest">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="70" title="Git">

<br><br>

**Python · aiogram · Telethon · aiohttp · SQLAlchemy · PostgreSQL · Alembic · APScheduler · pytest**

</div>

---

## 🗺️ Roadmap

- [x] Сбор с сайтов и из Telegram-каналов
- [x] Подбор: синонимы профессий, фильтры, ключевые слова, исключения
- [x] Защита от дублей, рекламы и мошеннических «вакансий»
- [x] Уведомления о новых вакансиях
- [x] Mini App: тёмная и светлая темы
- [x] ✉️ Письмо работодателю через ИИ
- [x] Подписка PRO и оплата
- [x] Процент совпадения в ленте

---

<div align="center">

## Нужен похожий бот для ваших задач?

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=2000&pause=500&color=FF1FA0&center=true&vCenter=true&width=500&lines=Напишите+мне+-+обсудим+любые+идеи!">

<br><br>

**Sony Fridmo**

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
