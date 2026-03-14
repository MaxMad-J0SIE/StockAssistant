# this will be the main file (a controller)
# it will make everything work

# NOTES:
#   1st - HEART (BACKEND) - NOT DONE
#       Opening and reading the csv (later changed for API) - csv opened and read (to be updated when API is integrated)
#       Refractor data to suit your needs
#       Evaluate data and think of an answer (buy, sell optionally short, long)
#       User_data file is to be copied to User_data_copy before every change (later updated for SQL)
#   2nd - SKIN (FRONTEND) - NOT DONE
#       App that lets the user interact with the program (not through CLI)
#       Nice looking with room to add additional functions
#   3rd - Security (SERVER) - NOT DONE
#       POSTGRESQL keeping requests and answers safe and ready to be retrieved
#       Login table that keeps all the passwords and logins safe (hashed)

from heart import Heart

class AppController:
    """
    Main controller for this project
    Coordinates between the Heart (BackEnd), Skin (FrontEnd) and Security (DB)
    """
    def __init__(self, connection = None):
        self.heart_con = connection

    def main(self):
        self.get_connection_to_heart()
        temp_read_holder = self.heart_con.read_data()
        # for testing purposes
        # for row in temp_read_holder:
        #     print(row)

    def get_connection_to_heart(self):
        if not self.heart_con:
            self.heart_con = Heart()

    def buy_stock(self):
        pass

    def sell_stock(self):
        pass

if __name__ == "__main__":
    app = AppController()
    app.main()