import sqlite3
from datetime import datetime, timedelta


class Database:
    """Класс для работы с базой данных"""
    
    def __init__(self, db_path='vacancies.db'):
        """Подключаемся к базе"""
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self):
        """Создаёт таблицы, если их нет"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS vacancies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                source TEXT,
                message_date DATETIME,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                is_sent BOOLEAN DEFAULT 0,
                keywords_matched TEXT
            )
        ''')
        
        # Таблица для счётчиков
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS counters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT UNIQUE,
                sent_count INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()
    
    def save_vacancy(self, text, source, message_date, keywords_matched):
        """Сохраняет вакансию в базу"""
        self.cursor.execute('''
            INSERT INTO vacancies (text, source, message_date, keywords_matched)
            VALUES (?, ?, ?, ?)
        ''', (text, source, message_date, keywords_matched))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def is_duplicate(self, text):
        """Проверяет, есть ли уже такая вакансия"""
        self.cursor.execute('''
            SELECT id FROM vacancies WHERE text = ? LIMIT 1
        ''', (text,))
        return self.cursor.fetchone() is not None
    
    def mark_as_sent(self, vacancy_id):
        """Отмечает вакансию как отправленную"""
        self.cursor.execute('''
            UPDATE vacancies SET is_sent = 1 WHERE id = ?
        ''', (vacancy_id,))
        self.conn.commit()
    
    def get_stats(self):
        """Возвращает статистику"""
        self.cursor.execute('SELECT COUNT(*) FROM vacancies')
        total = self.cursor.fetchone()[0]
        
        self.cursor.execute('SELECT COUNT(*) FROM vacancies WHERE is_sent = 1')
        sent = self.cursor.fetchone()[0]
        
        return {'total': total, 'sent': sent}
    
    def get_today_sent_count(self):
        """Сколько отправлено сегодня"""
        today = datetime.now().strftime('%Y-%m-%d')
        self.cursor.execute('SELECT sent_count FROM counters WHERE date = ?', (today,))
        result = self.cursor.fetchone()
        return result[0] if result else 0
    
    def increment_sent_count(self):
        """Увеличивает счётчик отправленных сегодня"""
        today = datetime.now().strftime('%Y-%m-%d')
        self.cursor.execute('''
            INSERT INTO counters (date, sent_count) VALUES (?, 1)
            ON CONFLICT(date) DO UPDATE SET sent_count = sent_count + 1
        ''', (today,))
        self.conn.commit()
    
    def clean_old(self, days=10):
        """Удаляет вакансии старше N дней"""
        cutoff = datetime.now() - timedelta(days=days)
        self.cursor.execute('''
            DELETE FROM vacancies WHERE added_date < ?
        ''', (cutoff,))
        self.conn.commit()
    
    def close(self):
        """Закрывает соединение с базой"""
        self.conn.close()
