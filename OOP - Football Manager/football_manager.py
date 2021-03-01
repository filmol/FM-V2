from team import Team
from league import League

class Fotball_Manager:
    """ Fotball Manager Game """

    def __init__(self):
        self.team = None
        self.league = League("Fotball League")

    def create_team(self) -> None:
        """ Creates a team """

        team_name = input("Skapa ett lagnamn: ")
        self.league.add_team(team_name)

    def print_teams(self) -> None:
        """ Prints the team name for each team """
        if self.league.print_teams() == False:
            print(self.league.name + " has no teams assigned yet, add one")
        else:
            for team in self.league.print_teams():
                print(team)

    def play_game(self) -> None:
        """ Handles the play matches part of the game """

        opposition_list = []
        for team in self.league.print_teams():
            if team != self.team:
                opposition_list.append(team)
        for team in opposition_list:
            print(team)
        team_name = input("Choose a team to play against from above: ")
        while [t for t in opposition_list if t.name == team_name] == []:
            team_name = input("Choose a team to play against from above: ")
        opposition = self.league.get_team(team_name)
        print(self.league.play(self.team,opposition))

    def get_team_info(self) -> None:
        """ Retrieves Team information """
        print("Team: " + self.team.name)
        print("Rating: " + str(round(float(self.team.get_TOT()))))
        self.get_coach()
        print("-"*50)
        print(self.team.name + " has the following players:")
        self.print_players()

    def print_players(self) -> None:
        """ Prints the player information for each player in the team """
        if self.team.print_players() == False:
            print(self.team.name + " has no __players assigned yet, add a few")
        else:
            for player in self.team.print_players():
                print(player)

    def get_coach(self) -> None:
        """ Prints the coach information """
        if self.team.get_coach() == False:
            print("This team has no coach assigned yet")
        else:
            print(self.team.get_coach())
             
    def remove_coach(self) -> None:
        """ Removes the coach from the team """
        if self.team.remove_coach() == True:
            print("Coach deleted")
        else:
            print("This team has no coach assigned yet") 
    
    def remove_player(self) -> None:
        """ Removes the player from the team """
        self.print_players()
        print("-"*50)
        player_nr = int(input("Write the shirt number of the player you want to remove: "))
        if self.team.remove_player(player_nr) == True:
            print("Player is deleted")
        else:
            print("No player with that nr")

    def add_player(self) -> None:
        """ Adds a player to the team with the input recieved """

        choice = "y"
        while choice == "y":
            name = input("Playername: ")
            position = input("Position: ")
            age = input("Age: ")
            while age.isdigit() == False:
                print("Age has to be a integer")
                age = input("Age: ")
            rating = input("Rating (0-99): ")
            while rating.isdigit() ==  False:
                print("Rating has to be a integer")
                rating = input("Rating (0-99): ")
            nr = input("Shirt Number: ")
            while nr.isdigit() == False:
                print("Shirt number has to be a integer")
                nr = input("Shirt Number: ")
                
            while self.team.add_player(name,age,position,rating,nr) == False:
                print("Number " + nr + " is already taken, please choose another one")    
                nr = input("Shirt Number: ") 
            print("Player added")
            choice = input("Add another player? (y/n) ")

        else:  
            print("Already 5 players in team, remove one first")
    
    def add_coach(self) -> None:
        """ Adds a coach to the team with the input recieved """

        if self.team.get_coach() == False:
            name = input("Coach name: ")
            age = input("Age: ")
            while age.isdigit() == False:
                print("Age has to be a integer")
                age = input("Age: ")
            style = input("Style (Defensive/Offensive): ")
            style = style.lower()
            while style != "defensive" and style != "offensive":
                print("Coach style has to be defensive or offensive")
                style = input("Style: ")
                style = style.lower()
            self.team.add_coach(name,age,style)

        else:
            print("The team already got a coach")

    def set_captain(self) -> None:
        """ Makes a player the team captain """

        self.print_players()
        print("-"*50)
        captain_nr = int(input("Write the shirt number of your upcoming captain: "))
        if self.team.set_captain(captain_nr) == False:
            print("There isn't a player in the squad with nr: " + str(captain_nr))
        else:
            print("Nr:" + str(captain_nr) + " is now your new captain")

    def print_menu(self) -> None:
        """ Prints a menu for Team mode """
        print("-"*50)
        print("Menu")
        print("Val 1: Play Game")
        print("Val 2: Add Player")
        print("Val 3: Add Coach")
        print("Val 4: Show Team")
        print("Val 5: Choose Captain")
        print("Val 6: Remove Player")
        print("Val 7: Remove Coach")
        print("Val 0: Go Back")

    def print_main_menu(self) -> None:
        """ Prints an inital Menu """
        print("-"*50)
        print("Menu")
        print("Val 1: Enter Team")
        print("Val 2: Create Team")
        print("Val 0: End")

    def main_menu(self) -> None:
        """ Handles the inputs and flow of the main_menu options.
            Starts the right function depending on user choice.
        """
        choice = None
        while choice != "0":
            self.print_main_menu()
            choice = input("Ange val: ")
            if choice == "1":
                print("Choose one of the following teams:")
                print("-"*50)
                self.print_teams()
                print("-"*50)
                team_name = input("Your team choice: ")
                self.team = self.league.get_team(team_name)
                self.print_menu
                self.menu()            
            elif choice == "2":
                self.create_team()
            elif choice == "0":
                print("Bye!")
            else:
                print("Ange ett korrekt menyalternativ!")

    def menu(self) -> None:
        """ Handles the inputs and flow of the Team mode options.
        Starts the right function depending on user choice.
        """
        choice = None
        while choice != "0":
            self.print_menu()
            choice = input("Ange val: ")
            print("-"*50)
            if choice == "1":
                self.play_game()            
            elif choice == "2":
                self.add_player()
            elif choice == "3":
                self.add_coach()
            elif choice == "4":
                self.get_team_info()            
            elif choice == "5":
                self.set_captain()            
            elif choice == "6":
                self.remove_player()
            elif choice == "7":
                self.team.remove_coach()
            elif choice == "0":
                print("Bye!")
            else:
                print("Ange ett korrekt menyalternativ!")
                print("-"*50)

    def welcome(self) -> None:
        """ Welcomes the user to the game and triggers the main_menu 
        Creates two pre-made Teams with 5 Players and a Coach. 
        """
        print("=" * 50)
        print("Welcome to Fotball Manager!")
        print("=" * 50)

        self.league.add_team("MFF")
        self.team = self.league.get_team("MFF")
        self.team.add_player("Johan Dahlin",35,"MV",70,1)
        self.team.add_player("Ola Toivonen",33,"FW",72,9)        
        self.team.add_player("Markus Rosenberg",35,"FW",75,10)
        self.team.add_player("Erdal Rakip",24,"CM",68,25)
        self.team.add_player("Oscar Lewicki",24,"CM",67,26)
        self.team.add_coach("Åge Haaland",65,"defensive")        
        
        self.league.add_team("HIF")
        self.team = self.league.get_team("HIF")
        self.team.add_player("Johan Wiland",35,"MV",70,2)
        self.team.add_player("Andreas Grankvist",35,"MB",70,1)
        self.team.add_player("Alexander Gerndt",33,"FW",72,9)        
        self.team.add_player("Rasmus Jönsson",35,"FW",75,10)
        self.team.add_player("Henrik Rydström",24,"CM",65,25)
        self.team.add_coach("Rickard Norling",65,"offensive")

        self.main_menu()  
        
game = Fotball_Manager()
game.welcome()