class Train:
   
    def __init__(self, name, fare, seats):

        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print(f"Only {self.seats} seats are available.\nHurry Up..")
    
    def fareinfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticket is booked. Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full.")

intercity = Train("Intercity Express: 52364", 2300, 150)
intercity.fareinfo()
intercity.bookticket()
intercity.getstatus()

