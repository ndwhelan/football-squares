import random
import sys
from typing import Iterable, List, Tuple, Union

import click
from terminaltables import AsciiTable

SCORE_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class PlayersAndCountsParamType(click.ParamType):
    name = "<text,number>"

    def convert(self, value, param, ctx):

        try:
            player, count = value.split(",")
        except ValueError:
            self.fail(
                f'Unable to parse name and number for "{value}". Are there two parts?',
                param,
                ctx,
            )

        try:
            return player, int(count)
        except ValueError:
            self.fail(f'Count "{count}" is not a valid whole number')


@click.command()
@click.option(
    "-t", "--teams", type=(str, str), help="The two teams that are competing",
)
@click.option(
    "-p",
    "--players",
    type=PlayersAndCountsParamType(),
    multiple=True,
    help="List of players and their number of squares separated by a comma "
    "Numbers of squares over 100 will result in an error. An 'X' will be filled "
    "in if there are not 100 squares."
    'Ex: -p Nick,10 -p "Slappy O\'Houlihan,20"',
)
def build_squares(teams: Tuple[str, str], players: Iterable[Tuple[str, int]]) -> None:
    """
    Small command line utility to create a random tables of football squares.
    Team along the top will be the table header. Other team is omitted.
    """
    team_list = list(teams)
    random.shuffle(team_list)
    player_array: List[str] = []
    for player, count in players:
        player_array += [player] * count

    if len(player_array) > 100:
        print("There are more than 100 squares", file=sys.stderr)
        exit(1)

    player_array += ["X"] * (100 - len(player_array))
    random.shuffle(player_array)

    assert len(player_array) == 100, "Something is wrong. There are too many squares"

    player_array_split: List[List[Union[str, int]]] = [
        player_array[i : i + 10] for i in range(0, len(player_array), 10)
    ]
    # Need copy, because we insert for blank
    top_score_values: List[Union[str, int]] = SCORE_VALUES.copy()
    top_score_values.insert(0, " ")  # Create a blank corner square

    for x in range(10):
        # Insert side scores
        player_array_split[x].insert(0, SCORE_VALUES[x])

    player_array_split.insert(0, top_score_values)  # Insert top scores

    table = AsciiTable(player_array_split, team_list[0])
    table.inner_row_border = True
    print(table.table)


if __name__ == "__main__":
    build_squares()
