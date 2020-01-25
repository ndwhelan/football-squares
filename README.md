# Football Squares Generator

Run with `python football-squares.py --help` for instructions.

Example run, with 100 "buys":

```
python football-sqaures.py -t Chiefs 49ers -p Nick,10 -p Joe,10 -p Bob,10 -p Jane,10 -p Rose,10 -p Jack,10 -p Jill,10 -p Joan,10 -p Brad,10 -p Katy,10
```

### Help Output

```
Usage: football-squares.py [OPTIONS]

  Small command line utility to create a random tables of football squares.
  Team along the top will be the table header. Other team is omitted.

Options:
  -t, --teams <TEXT TEXT>...   The two teams that are competing
  -p, --players <TEXT,NUMBER>  List of players and their number of squares
                               separated by a comma Numbers of squares over
                               100 will result in an error. An 'X' will be
                               filled in if there are not 100 squares.Ex: -p
                               Nick,10 -p "Slappy O'Houlihan,20"
  --help                       Show this message and exit.
```

Requires Python 3.6 or greater. `init.sh` will set things up if you have `pyenv` installed, and the dependencies in `requirements.txt`. Admittedly, it could use a `setup.py`.
