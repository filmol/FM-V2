from person import Person

class Player(Person):
    '''A Fotballplayer in the game
           
    Args:
        nr (int) : the shirt number of the player
        position (str) : the field position of the fotballplayer
        rating (int) : the rating of the player
    '''

    def __init__(self, nr: int, position: str, rating: int, *args, **kwargs) -> None:
        '''Creates an instance of Player
        '''
        self.position = position
        self.nr = nr
        self.rating = rating
        self.captain = False
        super().__init__(*args, **kwargs)

    def get_nr(self) -> int:
        '''Get the shirt number of a player

        Returns:
            int : the shirt number
        '''
        return self.nr

    def get_rating(self) -> int:
        '''Get the rating of a player

        Returns:
            int : the rating
        '''
        return self.rating    
        
    def get_captain_val(self) -> bool:
        '''Get the bool value of captain attribute

        Returns:
            bool : the value
        '''
        return self.captain    
        
    def set_captain(self, value:bool) -> None:
        '''Sets the bool value of captain

          Args:
            value (bool) : the new boolean value of captain
        '''
        self.captain = value

    def __str__(self) -> str:
        '''Print a readable version of the fotballplayer
        
        Returns:
            str : Information about the player
        '''
        if self.captain == False:
            return "Nr: {}, Player: {}, Age: {}, Position: {}, Rating: {}".format(self.nr, self.name, self.age, self.position, self.rating)  
        elif self.captain == True:
            return "Nr: {}, Player: {}, Age: {}, Position: {}, Rating: {} (Captain)".format(self.nr, self.name, self.age, self.position, self.rating)
