class LogEntry:
    def __init__(self,date:str, start_time:str, end_time:str, group_size:int, activity_code:str, note:str) -> None:
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.group_size = group_size
        self.activity_code = activity_code
        self.note = note
    def __repr__(self) -> str:
        return f"\nLogEntry:: Date: {self.date}, Start Time: {self.start_time}, End Time: {self.end_time}, Group Size: {self.group_size}, Activity Code: {self.activity_code}, Note: {self.note}\n"    
