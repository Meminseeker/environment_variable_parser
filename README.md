# Environment Variables Parser

This is a small Python project to deal with environment variables easily.

## Installation

Clone the project to your computer. To clone with SSH, use this:

```bash
git clone git@github.com:Meminseeker/environment_variable_parser.git
```

For other cloning types, visit [this](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories).

## Usage

```bash
# prints the value of the environment variable <VARIABLE_NAME> if found
python main.py <VARIABLE_NAME>

# It is case insensitive. Each of these prints the value of the environment variable 'HOME'
python main.py HOME
python main.py Home
python main.py home

# if the environment variable is 'PATH', all the path names are printed line by line
python main.py PATH

# if the variable name is not found, prints "There is no such environment variable: <NOT_FOUND_VARIABLE_NAME>"
python main.py <NOT_FOUND_VARIABLE_NAME>
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Important Note

The application is modified for some testing purposes and the README file is not representing the current version. Be aware of it!
