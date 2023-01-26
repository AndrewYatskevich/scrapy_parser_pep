import datetime as dt
import csv

from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).parents[1] / 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def __init__(self):
        self.pep_statuses = defaultdict(lambda: 0, {})

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.pep_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = BASE_DIR / file_name

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(['Статус,Количество'])
            for status, count in self.pep_statuses.items():
                writer.writerow([f'{status},{count}'])
            writer.writerow([f'Total,{sum(self.pep_statuses.values())}'])
