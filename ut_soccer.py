"""
soccer ut
"""
from soccer import Parser, SoccerRank


data = ["Lions 3, Snakes 3", \
        "Tarantulas 1, FC Awesome 0", \
        "Lions 1, FC Awesome 1", \
        "Tarantulas 3, Snakes 1", \
        "Lions 4, Grouches 0"]
p = Parser()
p.parse(data)
sr = SoccerRank(p.score_map)
result = sr.sort_scores()
expected = [('Tarantulas', 6), ('Lions', 5), ('FC Awesome', 1), ('Snakes', 1), ('Grouches', 0)]
assert(result == expected)
print "Simple case provided in the exercise:"
print "Given raw:\n", data, "\nexpected :\n", expected, "\nactual result:\n", result
print "--------"

data = ["Lions 3, Snakes 3"]
p = Parser()
p.parse(data)
sr = SoccerRank(p.score_map)
result = sr.sort_scores()
expected = [('Lions', 1), ('Snakes', 1)]
assert(result == expected)
print "Simple case single entry, tie:"
print "Given raw:\n", data, "\nexpected :\n", expected, "\nactual result:\n", result
print "--------"

data = ["Lions 0, Snakes 3"]
p = Parser()
p.parse(data)
sr = SoccerRank(p.score_map)
result = sr.sort_scores()
expected = [('Snakes', 3), ('Lions', 0)]
assert(result == expected)
print "Simple case single entry, one winner:"
print "Given raw:\n", data, "\nexpected :\n", expected, "\nactual result:\n", result
print "--------"

data = ["Snakes 3, Snakes 0"]
p = Parser()
p.parse(data)
sr = SoccerRank(p.score_map)
result = sr.sort_scores()
expected = [('Snakes', 3)]
print result
assert(result == expected)
print "Simple case single entry, single team. This case works too... TBD: need to fail such cases"
print "Given raw:\n", data, "\nexpected :\n", expected, "\nactual result:\n", result
print "--------"

