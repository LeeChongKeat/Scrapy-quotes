# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter


class QuotetutorialPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()
        pass

    def create_connection(self):
        self.conn = sqlite3.Connection("myquotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP Table if exists quotes_tb""")
        self.curr.execute(""" create table quotes_tb(
                            title text,
                            author text,
                            tag text
                            ) """)
        self.curr.execute("""INSERT INTO quotes_tb values (?,?,?)""", (
            1,
            2,
            3
        ))


    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline : " + item['title'][0])
        return item

    def store_db(self, item):
        print("store_db : " + item['title'][0])
        self.curr.execute(""" INSERT INTO quotes_tb values (?,?,?)""", (
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
