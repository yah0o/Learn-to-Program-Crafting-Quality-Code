# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

	The first parameter represents the rat to be initialized,
	the second parameter represents the 1-character symbol for the rat,
	the third parameter represents the row where the rat is located,
	and the fourth parameter represents the column where the rat is located.
     
        Initialize the rat's four instance variables:

        symbol: the 1-character symbol for the rat
        row: the row where the rat is located
        col: the column where the rat is located
        num_sprouts_eaten: the number of sprouts that
        this rat has eaten, which is initially 0.
        >>> rat = Rat('P', 1, 4)
        >>> rat.symbol
        'P'
        >>> rat.row
        1
        >>> rat.col
        4
        >>> rat.num_sprouts_eaten
        0
        """

        assert len(symbol) == 1, \
               'symbol is not 1-character.'

        self.symbol = symbol
        self.set_location(row, col)
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType
        The first parameter represents a rat,
        the second represents a row,
        and the third represents a column.
        Set the rat's row and col instance variables
        to the given row and column.
        
        >>> rat = Rat('P', 1, 4)
	>>> rat.set_location(3, 5)
        >>> rat.row
        3
        >>> rat.col
        5
        """

        assert row >= 0, \
               'row is negative.'
        assert col >= 0, \
               'col is negative.'

        self.row = row
        self.col = col

    def eat_sprout(self):
        """ (Rat) -> NoneType
        The first parameter represents a rat.
        Add one to the rat's instance variable num_sprouts_eaten. Yuck.
        
        >>> rat = Rat('P', 1, 4)
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """

        self.num_sprouts_eaten += 1

    def __str__(self):
        """ (Rat) -> str
        The parameter represents a rat.
        Return a string representation of the rat, in this format:
        symbol at (row, col) ate num_sprouts_eaten sprouts.

        >>> rat = Rat('J', 4, 3)
        >>> rat.eat_sprout()
        >>> rat.eat_sprout()
        >>> print(rat)
        J at (4, 3) ate 2 sprouts.
        """

        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)
    
    
class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType
        The first paramter represents the maze to be initialized,
        the second parameter represents the contents of the maze,
        the third parameter represents the first rat in the maze,
        and the fourth parameter represents the second rat in the maze.
        Initialize this maze's four instance variables:
        1) maze: a maze with contents specified by the second parameter.
        2) rat_1: the first rat in the maze.
        3) rat_2: the second rat in the maze.
        4) num_sprouts_left: the number of uneaten sprouts in this maze.
	
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                         ['#', '.', '.', '.', '.', '.', '#'], \
                         ['#', '.', '#', '#', '#', '.', '#'], \
                         ['#', '.', '.', '@', '#', '.', '#'], \
                         ['#', '@', '#', '.', '@', '.', '#'], \
                         ['#', '#', '#', '#', '#', '#', '#']], \
                         Rat('J', 1, 1), \
                         Rat('P', 1, 4))
	>>> maze.maze
        [['#', '#', '#', '#', '#', '#', '#'], ['#', 'J', '.', '.', 'P', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> maze.num_sprouts_left
        3
        """

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.maze[rat_1.row][rat_1.col] = rat_1.symbol
        self.maze[rat_2.row][rat_2.col] = rat_2.symbol

        num_sprouts_left = 0
        
        for row in maze:
            num_sprouts_left = num_sprouts_left + row.count(SPROUT)
        self.num_sprouts_left = num_sprouts_left

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool
	The first parameter represents a maze, the second represents a row,
	and the third represents a column.
	Return True if and only if there is a wall
	at the given row and column of the maze.
	
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                         ['#', '.', '.', '.', '.', '.', '#'], \
                         ['#', '.', '#', '#', '#', '.', '#'], \
                         ['#', '.', '.', '@', '#', '.', '#'], \
                         ['#', '@', '#', '.', '@', '.', '#'], \
                         ['#', '#', '#', '#', '#', '#', '#']], \
                         Rat('J', 1, 1), \
                         Rat('P', 1, 4))
        >>> maze.is_wall(0, 0)
        True
        >>> maze.is_wall(1, 1)
        False
        >>> maze.is_wall(1, 2)
        False
        >>> maze.is_wall(2, 1)
        False
        """

        return self.get_character(row, col) == WALL

    def get_character(self, row, col):
        """ (Maze, int, int) -> str
	The first parameter represents a maze, the second represents a row,
	and the third represents a column.

        Return the character in the maze at the given row and column.
        If there is a rat at that location,
        then its character should be returned rather than HALL.
        
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                         ['#', '.', '.', '.', '.', '.', '#'], \
                         ['#', '.', '#', '#', '#', '.', '#'], \
                         ['#', '.', '.', '@', '#', '.', '#'], \
                         ['#', '@', '#', '.', '@', '.', '#'], \
                         ['#', '#', '#', '#', '#', '#', '#']], \
                        Rat('J', 1, 1), \
                        Rat('P', 1, 4))
        >>> maze.get_character(0, 0)
        '#'
        >>> maze.get_character(1, 1)
        'J'
        >>> maze.get_character(1, 2)
        '.'
        >>> maze.get_character(1, 4)
        'P'
        >>> maze.get_character(4, 1)
        '@'
        """

        assert 0 <= row < len(self.maze), \
               'row not in the maze.'

        assert 0 <= col < len(self.maze[0]), \
               'col not in the maze.'

        return self.maze[row][col]

    def move(self, rat, vertical, horizontal):
        """ (Maze, Rat, int, int) -> bool
        The first parameter represents a maze, the second represents a rat,
        the third represents a vertical direction change (UP, NO_CHANGE or DOWN),
        and the fourth represents a horizontal direction change (LEFT, NO_CHANGE or RIGHT).

        Move the rat in the given direction, unless there is a wall in the way.
        Also, check for a Brussels sprout at that location and, if present:
        1) have the rat eat the Brussels sprout,
        2) make that location a HALL, and
        3) decrease the value that num_sprouts_left refers to by one.
        4) Return True if and only if there wasn't a wall in the way.
	
        >>> LEFT = -1
        >>> RIGHT = 1
        >>> NO_CHANGE = 0
        >>> UP = -1
        >>> DOWN = 1
        >>> rat_1 = Rat('J', 1, 1)
        >>> rat_2 = Rat('P', 1, 4)
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                         ['#', '.', '.', '.', '.', '.', '#'], \
                         ['#', '.', '#', '#', '#', '.', '#'], \
                         ['#', '.', '.', '@', '#', '.', '#'], \
                         ['#', '@', '#', '.', '@', '.', '#'], \
                         ['#', '#', '#', '#', '#', '#', '#']], \
                        rat_1, \
                        rat_2)
        >>> maze.move(rat_1, UP, NO_CHANGE)
        False
        >>> maze.move(rat_2, DOWN, NO_CHANGE)
        False
        >>> maze.move(rat_1, DOWN, NO_CHANGE)
        True
        >>> maze.move(rat_1, UP, NO_CHANGE)
        True
        >>> maze.move(rat_1, NO_CHANGE, LEFT)
        False
        >>> maze.move(rat_2, NO_CHANGE, RIGHT)
        True
        >>> maze.move(rat_2, NO_CHANGE, RIGHT)
        False
        >>> maze.move(rat_2, NO_CHANGE, LEFT)
        True
        >>> maze.move(rat_1, DOWN, RIGHT)
        False
        >>> maze.move(rat_2, DOWN, RIGHT)
        True
        >>> maze.move(rat_2, DOWN, NO_CHANGE)
        True
        >>> rat_2.num_sprouts_eaten
        0
        >>> maze.move(rat_2, DOWN, LEFT)
        True
        >>> rat_2.num_sprouts_eaten
        1
        >>> rat_2.row
        4
        >>> rat_2.col
        4
        >>> maze.get_character(rat_2.row, rat_2.col)
        'P'
        >>> maze.get_character(rat_2.row + UP, rat_2.col + RIGHT)
        '.'
        """

        assert vertical == UP or \
               vertical == NO_CHANGE or \
               vertical == DOWN, \
           'vertical direction wrong.'

        assert horizontal == UP or \
               horizontal == NO_CHANGE or \
               horizontal == DOWN, \
           'horizontal direction wrong.'
      
        new_row = rat.row + vertical
        new_col = rat.col + horizontal

        if self.is_wall(new_row, new_col):
            return False

        if self.get_character(new_row, new_col) == SPROUT:
            rat.eat_sprout()
            self.num_sprouts_left = self.num_sprouts_left - 1

        self.maze[rat.row][rat.col] = HALL

        rat.set_location(new_row, new_col)

        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

        return True

    def __str__(self):
        """ (Maze) -> str
        The parameter represents a maze.
        Return a string representation of the maze,
        using the format shown in this example:
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                         ['#', '.', '.', '.', '.', '.', '#'], \
                         ['#', '.', '#', '#', '#', '.', '#'], \
                         ['#', '.', '.', '@', '#', '.', '#'], \
                         ['#', '@', '#', '.', '@', '.', '#'], \
                         ['#', '#', '#', '#', '#', '#', '#']], \
                        Rat('J', 1, 1), \
                        Rat('P', 1, 4))
        >>> print(maze)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """

        result = ''
        for row in self.maze:
            for i in row:
                result = result + i
            result += '\n'
        return result + "{0}\n{1}".format(self.rat_1, self.rat_2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
