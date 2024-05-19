
from enum import Enum

class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class Friend:

    def __init__(self, user, priority):
        self.user = user
        self.priority = priority
        self.last_talked_to = None

    def change_priority(self, priority):
        self.priority = priority
    
    def get_priority(self):
        return self.priority

    def get_user(self):
        return self.user