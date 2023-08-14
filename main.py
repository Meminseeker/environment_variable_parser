import os
import sys

# get the system argument from the terminal
variable = sys.argv[1]
variable = variable.upper()  # make the variable uppercase

# check if the variable is an environment variable
if variable in os.environ:
    # get the value of the environment variable
    value = os.environ[variable]

    # check if the environment variable is 'PATH'
    if variable == "PATH":
        # split the value by ':' (columns)
        value = value.split(':')

        # print the splitted values, one line for each
        for splitted_value in value:
            print(splitted_value)

    # if the environment variable is not a specific one, do the default action
    else:
        print("{}".format(value)) # print the value

# check if the variable is KEYS, when it is not an environment variable
elif variable == "KEYS":
    # print the names of all environment variables
    for key in os.environ.keys():
        print(key)

# if variable is not identified, print an error message
else:
    print("There is no such environment variable: {}".format(variable))
