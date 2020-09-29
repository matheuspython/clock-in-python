from time import sleep

#I did it using class but it is optional

class clock:
    def __init__(self):
        self.hours = []
        self.minutes = []
        self.seconds = []
    
    def fill_times(self):
        self.filler = 0
        while self.filler !=61:
            self.seconds.append(self.filler)
            self.minutes.append(self.filler)
            self.filler += 1
        
        self.filler = 0

        while self.filler != 24:
            self.hours.append(self.filler)
            self.filler += 1

    def start_clock(self):
        self.zero = 0
        self.minutes_counter = 0
        self.hour_counter = 0
        self.seconds_counter = 0
        print('now its hours {} minutes {} and seconds {}'.format(self.hours[self.hour_counter], self.minutes[self.minutes_counter], self.seconds[self.seconds_counter]))
            
        while self.zero != 1:
        
            if self.seconds_counter == 60:
                self.minutes_counter += 1
                self.seconds_counter = 0

            if self.minutes_counter == 60:
                self.hour_counter +=1
                self.minutes_counter = 0

            self.seconds_counter += 1    
            print('now its hours {} minutes {} and seconds {}'.format(self.hours[self.hour_counter], self.minutes[self.minutes_counter], self.seconds[self.seconds_counter]))
            
            if self.hour_counter == 23 and self.minutes_counter == 59 and self.seconds_counter == 60:
                self.zero = 1
                print('now its hours {} minutes {} and seconds {}'.format(self.hours[0], self.minutes[0], self.seconds[0]))
                

clock = clock()
clock.fill_times()
clock.start_clock()

