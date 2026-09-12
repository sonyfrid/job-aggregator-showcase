from src.core.config import KEYWORDS, EXCLUDE, MUST_HAVE_QA, WORK_FORMATS


MUST_HAVE_STACK = [
    'javascript',
    'typescript',
    'js',
    'ts',
    'playwright',
]

MANUAL_LEVELS = [
    'middle manual',
    'senior manual',
    'мидл мануал',
    'сеньор мануал',
    'middle qa',
    'senior qa',
    'qa middle',
    'qa senior',
    'ведущий тестировщик',
    'старший тестировщик',
]

COLLECTION_MARKERS = [
    'подборка',
    'дайджест',
    'вакансии недели',
    'подборка вакансий',
    'топ вакансий',
    'свежие вакансии',
    'vacancies digest',
    'job digest',
]


def is_collection(text):
    text_lower = text.lower()
    return any(marker in text_lower for marker in COLLECTION_MARKERS)


def is_match(text):
    """Проверяет текст вакансии"""
    if not text:
        return False
    
    text_lower = text.lower()
    
    # Исключения
    for exclude in EXCLUDE:
        if exclude in text_lower:
            return False
    
    # Подборки
    if is_collection(text):
        return False
    
    # Формат: офис/гибрид без удалёнки — пропускаем
    has_remote = any(f in text_lower for f in WORK_FORMATS)
    has_office = any(word in text_lower for word in ['офис', 'office', 'гибрид', 'hybrid'])
    
    if has_office and not has_remote:
        return False
    
    # QA?
    has_qa = any(qa in text_lower for qa in MUST_HAVE_QA)
    if not has_qa:
        return False
    
    # Automation
    has_stack = any(stack in text_lower for stack in MUST_HAVE_STACK)
    if has_stack:
        return True
    
    # Manual Middle/Senior
    has_manual_level = any(level in text_lower for level in MANUAL_LEVELS)
    if has_manual_level:
        return True
    
    # Просто QA
    if 'qa' in text_lower or 'тестировщик' in text_lower:
        return True
    
    return False


def is_match_full(title, description=''):
    """Проверяет заголовок + описание"""
    if is_match(title):
        return True
    
    full_text = f"{title} {description}".lower()
    
    if is_collection(full_text):
        return False
    
    has_qa = any(qa in full_text for qa in MUST_HAVE_QA)
    has_stack = any(stack in full_text for stack in MUST_HAVE_STACK)
    has_remote = any(f in full_text for f in WORK_FORMATS)
    
    if has_qa and has_stack and has_remote:
        return True
    
    has_manual_level = any(level in full_text for level in MANUAL_LEVELS)
    if has_qa and has_manual_level and has_remote:
        return True
    
    if has_qa and has_remote:
        return True
    
    return False


def get_matched_keywords(text):
    text_lower = text.lower()
    matched = []
    
    for keyword in KEYWORDS:
        if keyword in text_lower:
            matched.append(keyword)
    
    return matched
