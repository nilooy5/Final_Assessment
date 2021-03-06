# takes a file and returns a list
def read_multi_dim_data(filename):
    file = None
    dataset = []

    try:
        file = open(filename, "r")

        while True:
            line = file.readline()
            if len(line) == 0 or line == "\n":
                break
            else:
                line = line.removesuffix("\n")
                xy = line.split(" ")
                for i in range(len(xy)):
                    xy[i] = float(xy[i])
                dataset.append(list(xy))
    except Exception as ex:
        print(ex.args)
    finally:
        if file:
            file.close()
    return dataset


# takes a list; formats & saves in file with dimensions
def write_to_file(dataset, dimension):
    formatted_dataset = stringify_dataset(dataset)
    print(formatted_dataset)
    filename = 'output_' + str(dimension) + 'D.txt'

    f = open(filename, 'w')
    f.write(formatted_dataset)
    f.close()

    print("output stored in file " + "\"" + filename + "\"")


# takes a list and returns a string with the list formatted
def stringify_dataset(dataset):
    formatted_dataset = ''''''
    for point, color in dataset:
        tuple_string = "("
        for item in point:
            tuple_string += (str(item) + ", ")
        tuple_string = tuple_string[:-2]
        tuple_string += ")"
        formatted_dataset += ("The unknown point " + tuple_string + " falls in " + color + " class\n")

    return formatted_dataset
