import requests

USERS_SHEETY_ENDPOINT = "https://api.sheety.co/45b16c9a9784d95e5305b68f0f4e7ec5/day39,40CheapFlightAlert/users"



class User_Entries:

    def __init__(self):
        self.user_emails_list = []


    def take_entries(self):
        if input("Do you want to enter any customers? type 'Y' for YES and 'N' for NO: ").upper() == "Y":
            repeat = True
        else:
            repeat = False

        while repeat:
            print("Welcome to Knight flight club")
            print("We find the best Flight deals for and notify you on Email")
            print("\n")
            first_name = input("Enter your First Name: ")
            last_name = input("Enter your Last Name: ")
            email = input("Enter your email : ")
            verify_email = input("Enter your email again: ")

            if email == verify_email:
                new_data = {
                    "user": {
                        "firstName": first_name,
                        "lastName": last_name,
                        "email": email
                    }
                }
                response = requests.post(url = f"{USERS_SHEETY_ENDPOINT}", json= new_data)
                response.raise_for_status()
                # print(response.json())
                more = input("\nDo you want to enter any more entries? type 'Y' for YES and 'N' for NO: ").upper()
                if more == "Y":
                    continue
                else:
                    repeat = False
            else:
                print("\nOOPS!!!   Emails entered do not match\nPlease enter the details again")

    def users_list(self):
        response = requests.get(USERS_SHEETY_ENDPOINT)
        users = response.json()["users"]

        self.user_emails_list = [user["email"] for user in users]

        # print(self.user_emails_list)
        return self.user_emails_list