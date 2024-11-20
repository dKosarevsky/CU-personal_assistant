import utils as ut

FINANCE_FILE = 'finance.json'


class FinanceRecord:
    def __init__(self, record_id, amount, category, date, description):
        self.id = record_id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description


class FinanceManager:
    def __init__(self):
        self.records = []
        self.load_records()

    def load_records(self):
        data = ut.load_data(FINANCE_FILE, [])
        self.records = [FinanceRecord(**record) for record in data]

