def get_big_array(file):
    with open(file) as file:
        array = [int(integer) for integer in file]
    return array