class Message:
    def __init__(self):
        self.message  = ''
    def set_message(self, message):
        self.message = message.capitalize() + ' BYE.'
        
m1 = Message()
m1.set_message('dsawsd')
print(m1.message)


    
    
