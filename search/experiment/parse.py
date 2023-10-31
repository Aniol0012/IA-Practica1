import sys
from optilog.running import parse_scenario, ParsingInfo

scenario_path = sys.argv[1]

parsing_info = ParsingInfo()
parsing_info.add_filter(
    name="cost",
    cast_to=int,
    expression=r"Path found with total cost of (\d+)",
)
parsing_info.add_filter(
    name="time",
    cast_to=float,
    expression=r"Path found with total cost of \d+ in (.*) seconds",
)
parsing_info.add_filter(
    name="expanded",
    cast_to=int,
    expression=r"Search nodes expanded: (\d+)",
)
parsing_info.add_filter(
    name="score",
    cast_to=int,
    expression=r"Pacman emerges victorious! Score: (\d+(\.\d+)?)",
)

df = parse_scenario(scenario_path, parsing_info, simplify_index=True)
df = df.drop(["seed"], axis=1, level=1)

print("\n======================================")
print("Times:")
print(df.xs("time", level=1, axis=1))

print("\n======================================")
print("Cost of the path:")
print(df.xs("cost", level=1, axis=1))

print("\n======================================")
print("Expanded nodes:")
print(df.xs("expanded", level=1, axis=1))

print("\n======================================")
print("Score:")
print(df.xs("score", level=1, axis=1))

df.to_excel("output.xlsx", float_format="%.10f")
