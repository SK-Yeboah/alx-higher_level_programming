#!/usr/bin/python3

"""Module defining the Base class."""
import json
import csv
import turtle

class Base:
    """Base  define the Base class."""

    __nb_objects = 0


    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as file:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_str)


    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: List represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    


    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set based on dictionary.

        Args:
            dictionary (dict): Dictionary containing attributes.

        Returns:
            Base: Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            raise ValueError(f"Unsupported class: {cls.__name__}")

        dummy_instance.update(**dictionary)  # Use update method to set attributes
        return dummy_instance


    @classmethod
    def load_from_file(cls):
        """Return a list of instances from the file <Class name>.json.

        Returns:
            list: List of instances.
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r') as file:
                json_str = file.read()
                list_of_dicts = cls.from_json_string(json_str)
                return [cls.create(**obj_dict) for obj_dict in list_of_dicts]
        except FileNotFoundError:
            return []
        
    def to_csv_row(self):
        """Return a CSV row representation of the instance.

        Returns:
            list: List representing the instance in CSV row format.
        """
        raise NotImplementedError("to_csv_row method must be implemented in derived classes")

    @classmethod
    def create_from_csv_row(cls, csv_row):
        """Create an instance based on a CSV row.

        Args:
            csv_row (list): CSV row representing an instance.

        Returns:
            Base: Instance with attributes set.
        """
        raise NotImplementedError("create_from_csv_row method must be implemented in derived classes")
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all the Rectangles and Squares.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.

        Returns:
            None
        """
        turtle.speed(2)  # Set turtle speed
        turtle.title("Drawing Rectangles and Squares")
        turtle.bgcolor("white")

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.done()

    def __init__(self, id = None):

        """Initialize a new instance of Base.

        Args:
            id (int): The id to be assigned. If None, auto-incremented.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    

