from datetime import datetime


class Operation:

    def __init__(self, data: dict):
        self.pk = data.get("id", None)
        self.state = data.get("state", None)
        self.date = datetime.fromisoformat(data.get("date", "2019-07-15T11:47:40.496961"))
        try:
            self.amount = data["operationAmount"]["amount"]
        except:
            self.amount = '0'
        try:
            self.currency = data["operationAmount"]["currency"]["name"]
        except:
            self.currency = 'Null'
        self.description = data.get("description", None)
        self._from = data.get("from", None)
        self.to = data.get("to", None)
