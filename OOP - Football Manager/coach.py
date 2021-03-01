from person import Person

class Coach(Person):
    '''A Coach in the game

    Args:
        style (str) : the fotball style of the coach
    '''

    def __init__(self, style: str, *args, **kwargs) -> None:
        '''Creates an instance of Coach
        '''
        self.__style = style
        super().__init__(*args, **kwargs)

    def get_style(self) -> str:
        '''Get the style of the coach

        Returns:
            str : the style of the coach
        '''
        return self.__style

    def __str__(self) -> str:
        '''Print a readable version of the coach
        
        Returns:
            str : Information about the coach
        '''
        return "Coach: {}, Age: {}, is known for playing {} fotball".format(self.name, self.age, self.__style)
