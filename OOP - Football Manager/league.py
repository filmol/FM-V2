from player import Player
from coach import Coach
from team import Team
import random  

class League():
    '''Represents the league of the game which includes all the teams

    Args:
        name (str) : the name of the league
    '''

    def __init__(self, name: str) -> None:
        ''' Creates an instance of the league 
            - __teams (list[Team]) : list of Team instances
        '''
        self.name = name
        self.__teams = []

    def add_team(self,name : str) -> None:
        """
        Creates a new Team instance with input.
        Appends the new Team to the legues __team list.

        Args:
            name (str) : The name of the new team
        """
        new_team = Team(name)
        self.__teams.append(new_team) 

    def print_teams(self) -> list:
        """
        Accesses the _teams list

        Returns:
            list : a list of the Teams
        """
        if self.__teams == []:
            return False
        else:
            return self.__teams

    def remove_team(self,team_name:int) -> bool:
        """ Removes the right team by comparing the name input

        Args:
            team_name (str) : the team name of the team to be removed

        Returns:
            bool : value symbolizes if the team_name was found or not
        """
        for team in self.__teams:
            if team.name == team_name:
                self.__teams.remove(team)
                return True
        return False
        
    def get_team(self,team_name:str) -> Team:
        """
        Loops through the _teams list to find the right team

        Args:
            team_name (str) : The name of the team to get

        Returns:
            Team : the Team instance wanted
        """
        if self.__teams == []:
            return False
        else:
            for team in self.__teams:
                if team.name == team_name:
                    return team

    def play(self,team:Team, opposition:Team) -> str:
        """
        Function to play a game between two teams (team VS opposition).
        Retrieves the players for each team.
        Checks if both team has a full squad of 5 players to play the game and if a coach is present.

        Args:
            team (Team) : The user Team instance
            opposition (Team) : The copmuter Team instance 

        Returns:
            str : The game result based on the TOT of the Team instances.
        """
        Team1 = team.print_players()
        Team2 = opposition.print_players()
        
        if len(Team1) != 5 or len(Team2) != 5:
            return "Team has to consits of 5 players, " + team.name +  ": " + str(len(Team1)) + ", " + opposition.name + ": " + str(len(Team2))
        elif team.get_coach() == False:
            return "The team has to have a coach, add a coach before playing"
        else:
            T1 = team.get_TOT()
            T2 = opposition.get_TOT()
            T1 = random.uniform(0.8,1.1)*float(T1) 
            T2 = random.uniform(0.8,1.1)*float(T2)
            my_coach = team.get_coach()

            if float(T1) > float(T2):
                if my_coach.get_style() == "defensive":
                    return "Game result: " + team.name + " 1 - 0 " + opposition.name
                elif my_coach.get_style() == "offensive":  
                    return "Game result: " + team.name + " 3 - 1 " + opposition.name
            else: 
                if my_coach.get_style() == "defensive":
                    return "Game result: " + team.name + " 0 - 1 " + opposition.name
                elif my_coach.get_style() == "offensive":  
                    return "Game result: " + team.name + " 3 - 5 " + opposition.name
