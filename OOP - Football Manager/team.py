from player import Player
from coach import Coach

class Team():
    '''Represents a Team
        
    Args:
        name (str) : the name of the player
    '''

    def __init__(self, name: str) -> None:
        ''' Creates an instance of a Team
        + TOT (int) : The average rating of all players combined (Team rating) 
        - __players (list[Player]) : list of Player instances
        - __coach (Coach) : Value of None or a Coach instance
        '''
        self.name = name
        self.__players = []
        self.__coach = None
        self.TOT = 0
        
    def get_name(self) -> str:
        '''Get the name of the team

        Returns: 
            str : The name of the team
        '''
        return self.name

    def set_name(self, name: str) -> str:
        '''Set the name of the team

        Args:
            name (str) : the new name of the team

        Returns:
            str : the name of the team
        '''
        self.name = name
        return self.name

    def add_player(self,name: str,age: int,position: str,rating: int,nr: int) -> None:
        """
        Cheks if shirt number input is already taken.
        Creates a new Player instance with input.        
        Updates the Teams new TOT value.
        Appends Player to the Teams __player list.
        """
        for player in self.__players:
            if player.get_nr() == int(nr):
                return False
        new_player = Player(int(nr),position,int(rating),name,int(age))
        self.TOT+=int(rating)
        self.__players.append(new_player) 
    
    def add_coach(self,name: str,age: int,style: str) -> None:
        """
        Creates a new Coach instance with input.
        Team gets the coach instance assigned as their new coach.       
        """
        coach = Coach(style,name,age)
        self.__coach = coach

    def print_players(self) -> list:
        """
        Loops through list of players and sorts it by number

        Returns:
            list : a sorted list of players
        """
        if self.__players == []:
            return False
        else:
            player_list = []
            for player in self.__players:
                player_list.append(player)
                player_list.sort(key=lambda x: x.nr)
            return player_list

    def remove_player(self, player_nr:int) -> bool:
        """
        Removes the right player by comparing the number input with every players number
        Updates the Teams new TOT value.

        Args:
            player_nr (int) : the shirt nr of the player to be removed

        Returns:
            bool : value symbolizes if the player_nr was found or not
        """
        for player in self.__players:
            if player.get_nr() == player_nr:
                self.TOT -= player.get_rating()
                self.__players.remove(player)
                return True
        return False

    def remove_coach(self) -> bool:
        """
        Resets the Teams coach value to None

        Returns:
            bool : value symbolizes if the coach was removed or if it already was None
        """
        if self.__coach == None:
            return False
        else:
            self.__coach = None
            return True

    def get_coach(self) -> Coach:
        '''Get the Teams coach object

        Returns: 
            Coach : the Coach instance wanted
        '''
        if self.__coach == None:
            return False
        else:
            return self.__coach
        
    def set_captain(self, captain_nr: int) -> bool:
        """ Resets all captain atributtes to False
            Compares shirt nr wth input nr to find the player wanted as captain

        Args:
            captain_nr (int) : the shirt nr of the player to be the new captain

        Returns: 
            bool : value symbolizes if the shir nr was found and new captain was assigned

        """
        for player in self.__players:
            player.set_captain(False)

        for player in self.__players:
            if player.get_nr() == captain_nr:             
                player.set_captain(True)
                return True
        return False

    def get_TOT(self) -> str:
        """ Checks if TOT isn't equal to 0.
            Then devides the TOT with the number of players to get an average score for team total
        Returns: 
            str : the new TOT value
        """
        if self.TOT != 0:
            total = self.TOT / len(self.__players)
            return str(total)
        else:
            return str(self.TOT)

    def __str__(self) -> str:
        '''Print a readable version of the team name'''
        return "{}".format(self.name)
