<p align="center">
  <img alt="Progress Quest" src="http://progressquest.com/pq.png">
</p>

Relive the great adventure… this time in the terminal realm!

- Progress Quest site:  http://progressquest.com/
- Online version:       http://progressquest.com/play/
- Original version:     https://bitbucket.org/grumdrig/pq

## Features

- Faithful port of the game logic.
- Ideal to run on your server.
- Saves with backups to `$XDG_CONFIG_HOME/pqcli/save.dat`, which defaults to `C:/Users/<username>/.config/pqcli/` on Windows and `/home/<username>/.config/pqcli/` on Unix.

## How to install

If you have Python 3.9 or later, just run `pip install --user pqcli` and you're good to go!
Then type `pqcli` to run the game.

In case if you want to use the git version, the process is just a bit more complex:

```console
$ git clone https://github.com/surgical-duck/pq-cli.git
$ cd pq-cli
$ pip install --user .
```

## Run with flags
`python -m pqcli ...`

`--curses` Rich and colorful, default.

`--basic` Minimal UI, suitable for raw grind.

`--load-save <int>` to instantly start playing on the specified character in the roster.

`--list-saves` List saved characters and exit.

`--no-colors` Disable color highlighting in curses interface.

`--no-save` No progress will be saved.


Curses interface:

![Screenshot](screen-curses-logo.png)
![Screenshot](screen-curses.png)

Basic interface:

![Screenshot](screen-basic.png)


## Contributing

```sh
# Clone the repository:
git clone https://github.com/surgical-duck/pq-cli.git
cd pq-cli

# Install to a local venv:
poetry install

# Install pre-commit hooks:
poetry run pre-commit install

# Enter the venv:
poetry shell
```

This project uses [poetry](https://python-poetry.org/) for packaging.
Install instructions are available at [poetry#installation](https://python-poetry.org/docs/#installation).

## Troubleshooting

### `_curses.error: init_pair() returned ERR`

If running on Linux and you get the error `_curses.error: init_pair() returned ERR`,
try making sure that your `$TERM` variable is set to a value which supports
256 colors, such as via the following:

    TERM=xterm-256color pqcli

