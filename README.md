# Football Squares Generator

Run with `python football-squares.py --help` for instructions.

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