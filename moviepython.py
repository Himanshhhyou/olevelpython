import time
movies  = {
        "kakuda" : 200,
        "laxmii":300,
        "rajmahal" : 400
}
for i in movies:
    print(f"{i} ===> {movies[i]}rs.")
print("*"*20)
revenue  = 0
totalSeat = 100
userBooking = {}

while totalSeat > 0:
    print(f"Available Seats: {totalSeat}")
    m = input("Enter Movie name: ")
    
    print("Searching for movie...")
    time.sleep(3)
    for movie in movies:
        if m == movie:
            s = int(input("Enter seat: "))
            print("Wait while we are confirming your seat...")
            time.sleep(3)
            if totalSeat >=s:
                print("\nStatus: Confirm")
                totalSeat = totalSeat - s
                revenue = revenue + movies[m] * s
                break
            else:
                print("\nStatus : Failed\nReason: Not enough seats")
                break
    else:
        print(f"\nStatus : Failed\nReason: {m} movie  not available")
else:
    print("HouseFull")
p = input("Enter admin password")
if p == str(1234321):
     print(f"Revenue : {revenue}\n")
    


            
