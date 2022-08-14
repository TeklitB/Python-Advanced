
class TimeInterval:
    def __init__(self, h, m, s):
        if not isinstance(h, int):
            raise Exception("Hour is not a number")
        if not isinstance(m, int):
            raise Exception("Hour is not a number")
        if not isinstance(s, int):
            raise Exception("Hour is not a number")
        self.hour = h
        self.minute = m
        self.second = s
    
    def __str__(self):
        return f"{self.hour}:{self.minutes}:{self.second}"
    
    def __add__(self, other):
        if isinstance(other, TimeInterval):
            (h, m, s) = TimeInterval.add_time_interval(self.hour, self.minute, self.second, other.hour, other.minute, other.second)
            more_minutes = s // 60
            seconds = s % 60
            more_hours = m // 60
            minutes = (m + more_minutes) % 60
            hours = (h + more_hours) % 24
        
        if isinstance(other, int):
            more_minutes = (self.second + other) // 60
            seconds = (self.second + other) % 60
            more_hours = (self.minute + more_minutes) // 60
            minutes = (self.minute + more_minutes) % 60
            hours = (self.hour + more_hours) % 24
        
        return f"{hours}:{minutes}:{seconds}"

    def __sub__(self, other):
        if isinstance(other, TimeInterval):
            if self.hour >= other.hour:
                (h, m, s) = TimeInterval.add_time_interval(self.hour, self.minute, self.second, -other.hour, -other.minute, -other.second)
            else:
                (h, m, s) = TimeInterval.add_time_interval(other.hour, other.minute, other.second, -self.hour, -self.minute, -self.second)
            
            sec = s if s >= 0 else s + 60
            m = m if sec >= 0 else m - 1
            min = m if m >= 0 else m + 60
            h = h if m >= 0 else h - 1
            hr = h

        if isinstance(other, int):
            sec = (self.second - other) if (self.second - other) >= 0 else (self.second - other + 60)
            min = self.minute if (self.second - other) >= 0 else self.minute - 1
            hr = self.hour if (self.minute >= 0) else self.hour - 1

        
        return f"{hr}:{min}:{sec}"

    def __mul__(self, other):
        if isinstance(other, TimeInterval):
            more_sec = (self.second * other.second) // 60
            sec = (self.second * other.second) % 60
            more_hr = (self.minute * other.minute + more_sec) // 60
            min = (self.minute * other.minute + more_sec) % 60
            hr = self.hour * other.hour + more_hr
        
        if isinstance(other, int):
            more_minutes = (self.second * other) // 60
            sec = (self.second * other) % 60
            more_hours = (self.minute * other + more_minutes) // 60
            min = (self.minute * other + more_minutes) % 60
            hr = self.hour * other + more_hours
        
        return f"{hr}:{min}:{sec}"
    
    @classmethod
    def add_time_interval(cls, h1, m1, s1, h2, m2, s2):
        return (h1 + h2, m1 + m2, s1 + s2)
        

fti = TimeInterval(21, 58, 50)
sti = TimeInterval(1, 45, 22)
print(fti + sti)
print(fti - sti)
print(fti * sti)

# Multiply time interval by constant number value
print(fti * 2)

# Add or subtract second from the time interval
print(fti + 62)
print(fti - 62)