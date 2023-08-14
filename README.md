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
# prints the value of the environment variable 'HOME'
python main.py HOME

# these also print the value of the environment variable 'HOME'; it is case insensitive
python main.py home
python main.py hoME

# for the environment variable 'PATH', it splits the all path names and prints them line by line
python main.py PATH

# if the variable name is not found, prints "There is no such environment variable: VARIABLE_NAME"
python main.py VARIABLE_NAME
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
