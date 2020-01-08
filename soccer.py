"""
Usage:
  python soccer.py < sample-input.txt
  sample-input.txt | python soccer.py
  python soccer.py --file sample-input.txt


Assumptions:
  1. I am not ignoring the case of team names.
    Snakes is different than SNAKES.
  2. Input is valid.
  3. The number of teams and data cannot be too large.
    I am loading the data in memory and then parsing it.

Testing:
  Simple unit test: ut_soccer.py
  Basic functional test: soccer_functional_test.py


TBD:
1. Did not spend a lot of time on various cases except base ones.
2. No validation as the question mentioned valid input only.
3. I would split this into multiple files.
4. I would comment better on each method and specify more details.
  Used decent naming convention and sensible names.
5. Indentation needs improvement.


Total time: about 1hr 45 minutes.
Times worked on:
  parser class about 30 minutes.
  stdin part about 30, been a while since I used argparse, had to Google.
  SoccerRank class (essentially the main logic) took about 15 minutes.
    I did not implement the sorting algorithm itself, just used the
    sorted function with lambda.
  Test script about 25 minutes.
"""
import argparse
import re

class Parser(object):
  """
  """
  def __init__(self):
    """
    initializer.
    """
    self.regex = "(.*) ([\d]+)"
    self.score_map = {}

  def parse_scores(self, text):
    """
    Args:
      text(str): team info.
    Returns:
      list: [teamname, score]
    """
    r  = re.search(self.regex, text)
    # skipping the validation here.
    return [r.group(1), int(r.group(2))]

  def parse(self, text):
    """
    Args:
      text (str): input string blob.
    Returns:
      dict: Hash map of the form:
        {<team name>: <team score int>}
    """
    # No validation of the input required
    # otherwise, we will need extra code to
    # validate the steps.
    for line in text:
      t1_info, t2_info =  line.strip().split(",")
      name_1, score_1 = self.parse_scores(t1_info)
      name_2, score_2 = self.parse_scores(t2_info)
      name_1 = name_1.strip()
      name_2 = name_2.strip()
      if score_1 > score_2:
        self.add_winner(name_1)
        self.add_loser(name_2)
      elif score_1 < score_2:
        self.add_winner(name_2)
        self.add_loser(name_1)
      else:
        #tie
        self.add_tie(name_1)
        self.add_tie(name_2)

    return self.score_map

  def add_winner(self, name):
    """
    Args:
      name(str): Name of the team.
    """
    if name in self.score_map:
      # TBD: make 3 constant
      self.score_map[name]  += 3
    else:
      self.score_map[name] = 3

  def add_tie(self, name):
    """
    Args:
      name(str): Name of the team.
    """
    if name in self.score_map:
      # TBD: make 3 constant
      self.score_map[name]  += 1
    else:
      self.score_map[name] = 1

  def add_loser(self, name):
    """
    Args:
      name(str): Name of the team.
    """
    if name in self.score_map:
      # TBD: make 3 constant
      self.score_map[name]  += 0
    else:
      self.score_map[name] = 0


class SoccerRank(object):
  """
  Main class to get the score map and write the output to file.
  """
  def __init__(self, score_map):
    """
    """
    self.score_map = score_map

  def sort_scores(self):
    """
    Main logic to sort the score map.
    1. First sort the teams by highest score
    2. If the scores are the same then sort by alphabetical order
      of the name.
    Returns:
      list: list of the tuples of sorted scores.
    """
    # If the language didn't have this sorted feature, then, I would
    # I would have to implement either merge sort or quick sort.
    return sorted(self.score_map.items(), key=lambda x: (-x[1], x[0]))

  def write_output(self, **kwargs):
    """
    Args:
      kwargs:
        outfile(str): Output file name.
    """
    outfile = kwargs.get("outfile", "expected-output.txt")
    with open(outfile, "w") as f:
      for i, score in enumerate(self.sort_scores()):
        f.write("{}. {}, {} pts\n".format(i+1, score[0], score[1]))


if __name__ == "__main__":
  """
  Usage:
    see comment at the top.
  """
  parser = argparse.ArgumentParser(description='Soccer rank program')
  parser.add_argument('-i', '--file', type=argparse.FileType('r'), default='-')
  args = parser.parse_args()
  soccer_data = ""
  while True:
    data = args.file.read()
    if not data:
      break
    soccer_data += data
  lines = soccer_data.strip().split("\n")
  data_parser = Parser()
  data_parser.parse(lines)
  soccer_rank = SoccerRank(data_parser.score_map)
  soccer_rank.write_output()
