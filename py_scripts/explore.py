import numpy as np

def avg_grades_one_column(data, column, num_choices):
    """Calculate the average grades for different categories in a single column, 
    returning a numpy array of the averages for each of the different category possibilities.

    Args:
        data (pd dataframe): Dataframe used to get averages
        column (index): The column to average over
        num_choices (integer): Cardinality of values

    Returns:
        Numpy array: Array of the average grades for each possible unique category in column
    """
    import numpy as np
    array = np.array([])
    for i in np.arange(num_choices):
        array = np.append(array, data.query(f"`{column}` == {i + 1}").loc[:, 'GRADE'].mean())
    return array


# def say_hi(name: str) -> None:
#     """Function to greet

#     Parameters
#     ----------
#     name : str
#         Your name

#     Examples
#     --------
#     >>> from py_scripts.script_1 import say_hi
#     >>> say_hi("Badr MOUFAD")
#     Hi Badr MOUFAD!
#     """

#     print(f"Hi {name}!")
#     return