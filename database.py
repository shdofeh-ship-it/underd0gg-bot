import aiosqlite

DB_NAME = "underd0gg.db"


async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:

        # Пользователи
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            shadow_id TEXT UNIQUE,
            joined_at TEXT,
            wins INTEGER DEFAULT 0,
            participations INTEGER DEFAULT 0,
            notifications INTEGER DEFAULT 1
        )
        """)

        # Розыгрыши
        await db.execute("""
        CREATE TABLE IF NOT EXISTS giveaways(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            prize TEXT NOT NULL,
            active INTEGER DEFAULT 1,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Участники
        await db.execute("""
        CREATE TABLE IF NOT EXISTS participants(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            giveaway_id INTEGER,
            user_id INTEGER,
            UNIQUE(giveaway_id, user_id)
        )
        """)

        # Победители
        await db.execute("""
        CREATE TABLE IF NOT EXISTS winners(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            giveaway_id INTEGER,
            user_id INTEGER,
            won_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Промокоды
        await db.execute("""
        CREATE TABLE IF NOT EXISTS promo_codes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT UNIQUE,
            reward TEXT,
            max_uses INTEGER,
            used_count INTEGER DEFAULT 0
        )
        """)

        # Использованные промокоды
        await db.execute("""
        CREATE TABLE IF NOT EXISTS used_promos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            promo_id INTEGER,
            user_id INTEGER,
            UNIQUE(promo_id, user_id)
        )
        """)

        await db.commit()
