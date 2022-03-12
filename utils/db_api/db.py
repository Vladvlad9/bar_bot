from sqlite3 import *
from data.config import DATABASE


class DBApi(object):

    def __init__(self) -> None:
        self.__conn: Connection = connect(DATABASE)
        self.__cur: Cursor = self.__conn.cursor()

    async def create_roles_table(self) -> None:
        """CREATE ROLES TABLE"""
        self.__cur.execute('''
            CREATE TABLE IF NOT EXISTS
            roles(
                role TEXT PRIMARY KEY
            )
        ''')
        self.__conn.commit()

    async def create_users_table(self) -> None:
        """CREATE USER TABLES"""
        self.__cur.execute('''
            CREATE TABLE IF NOT EXISTS
            users(
                user_id INTEGER PRIMARY KEY,
                role TEXT NOT NULL,
                FOREIGN KEY (role) REFERENCES roles(role)
            )
        ''')
        self.__conn.commit()

    async def create_categories_table(self) -> None:
        """CREATE CATEGORIES TABLE"""
        self.__cur.execute('''
            CREATE TABLE IF NOT EXISTS
            categories(
                category TEXT PRIMARY KEY
            )
        ''')
        self.__conn.commit()

    async def create_subcategories_table(self) -> None:
        """CREATE SUBCATEGORIES TABLE"""
        self.__cur.execute('''
            CREATE TABLE IF NOT EXISTS
            subcategories(
                subcategory TEXT PRIMARY KEY,
                category TEXT NOT NULL,
                FOREIGN KEY (category) REFERENCES categories(category)
            )
        ''')
        self.__conn.commit()

    async def create_products_table(self) -> None:
        """CREATE PRODUCTS TABLE"""
        self.__cur.execute('''
            CREATE TABLE IF NOT EXISTS
            products(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                media_id TEXT,
                price INTEGER NOT NULL,
                subcategory TEXT,
                FOREIGN KEY (subcategory) REFERENCES subcategories(subcategory)
            )
        ''')
        self.__conn.commit()

    async def check_user(self, user_id: int) -> bool:
        """CHECK USER EXISTS"""
        self.__cur.execute('''
            SELECT user_id
            FROM users
            WHERE user_id = ?
        ''', (user_id,))
        return bool(self.__cur.fetchone())

    async def add_new_user(self, user_id: int, role: str = "user") -> bool:
        """ADD NEW USER"""
        try:
            self.__cur.execute('''
                INSERT INTO users(
                    user_id,
                    role
                )
                VALUES(?, ?)
            ''', (user_id, role))
            self.__conn.commit()
        except IntegrityError:
            return False
        else:
            return True

    async def change_user_role(self, user_id: int, new_role: str) -> None:
        """EDIT USER ROLE"""
        self.__cur.execute('''
            UPDATE users
            SET role = ?
            WHERE user_id = ?
        ''', (new_role, user_id))
        self.__conn.commit()

    async def add_category(self, category: str) -> bool:
        """ADD NEW CATEGORY"""
        print(category)
        try:
            self.__cur.execute('''
                INSERT INTO
                categories(
                    category
                )
                VALUES(?)
            ''', (category, ))
            self.__conn.commit()
        except IntegrityError:
            return False
        else:
            return True

    async def add_subcategory(self, category: str, subcategory: str) -> bool:
        """ADD NEW SUBCATEGORY"""
        try:
            self.__cur.execute('''
                        INSERT INTO
                        subcategories(
                            category,
                            subcategory
                        )
                        VALUES(?, ?)
                    ''', (category, subcategory))
            self.__conn.commit()
        except IntegrityError:
            return False
        else:
            return True

    async def add_product(self, title: str, description: str, price: int, subcategory: str, media_id: str = None) -> bool:
        """ADD PRODUCT TO SUBCATEGORY"""
        try:
            self.__cur.execute('''
                INSERT INTO products(
                    title,
                    description,
                    price,
                    media_id,
                    subcategory
                )
                VALUES(?, ?, ?, ?, ?)
            ''', (title, description, price, media_id, subcategory))
            self.__conn.commit()
        except IntegrityError:
            return False
        else:
            return True

    async def get_subcategories(self, category: str = None) -> tuple:
        """GET ALL SUBCATEGORIES FOR CATEGORY"""
        if category:
            self.__cur.execute('''
                SELECT subcategory
                FROM subcategories
                WHERE category = ?
            ''', (category, ))
        else:
            self.__cur.execute('''
                SELECT subcategory
                FROM subcategories
            ''')
        return tuple([subcategory[0] for subcategory in self.__cur.fetchall()])

    async def get_all_roles(self) -> tuple:
        """GET ALL ROLES"""
        self.__cur.execute('''
            SELECT role
            FROM roles
        ''')
        return tuple([role[0] for role in self.__cur.fetchall()])

    async def get_all_admins(self) -> tuple:
        """GET ALL ADMINS FROM DATABASE"""
        self.__cur.execute('''
            SELECT user_id
            FROM users
            WHERE role = ?
        ''', ("admin", ))
        return tuple([admin[0] for admin in self.__cur.fetchall()])

    async def get_products(self, subcategory: str) -> tuple:
        """GET ALL PRODUCTS FOR SUBCATEGORY FROM DATABASE"""
        self.__cur.execute('''
            SELECT *
            FROM products
            WHERE subcategory = ?
        ''', (subcategory, ))
        return tuple(self.__cur.fetchall())

    async def get_product(self, product_id: int) -> tuple:
        """GET ONE PRODUCT FROM DATABASE"""
        self.__cur.execute('''
            SELECT *
            FROM products
            WHERE id = ?
        ''', (product_id, ))
        return tuple(self.__cur.fetchone())

    async def add_new_photo_main_menu(self, photo: str, name_db) -> bool:
        try:
            add_photo = f'INSERT INTO {name_db}(photo) VALUES("{photo}")'
            self.__cur.execute(add_photo)
            self.__conn.commit()
        except IntegrityError:
            return False
        else:
            return True

    async def get_photo_main_menu(self, name_db: str):
        self.__cur.execute('SELECT photo '
                           f'FROM {name_db}')
        return self.__cur.fetchall()

    async def get_stock(self):
        self.__cur.execute('SELECT * '
                           f'FROM stock')
        return self.__cur.fetchall()

    async def add_stock(self, photo: str, description: str) -> bool:
        try:
            self.__cur.execute('''
                        INSERT INTO
                        stock(
                            photo,
                            description
                        )
                        VALUES(?, ?)
                    ''', (photo, description))
            self.__conn.commit()
        except IntegrityError:
            return False
        else:
            return True

    async def add_booking_user(self, user_id, lname, fname, date, time, number_people):
        try:
            self.__cur.execute('''
                        INSERT INTO
                        booking(
                            user_id,
                            lastName,
                            firstName,
                            date,
                            time,
                            number_people
                        )
                        VALUES(?, ?, ?, ?, ?, ?)
                    ''', (user_id, lname, fname, date, time, number_people))
            self.__conn.commit()
        except IntegrityError:
            return False
        else:
            return True


    async def create_all_database(self) -> None:
        """CREATE DATABASE"""
        await self.create_roles_table()
        await self.create_users_table()
        await self.create_categories_table()
        await self.create_subcategories_table()
        await self.create_products_table()