import pathlib

from optilog.running import RunningScenario
from optilog.blackbox import ExecutionConstraints, RunSolver

EXPERIMENT_DIR = pathlib.Path(__file__).parent.resolve()

experiments = [
    {
        "name": "search",
        "algorithms": {
            "bfs": str(EXPERIMENT_DIR / "algs" / "bfs.sh"),
            "dfs": str(EXPERIMENT_DIR / "algs" / "dfs.sh"),
            "ucs": str(EXPERIMENT_DIR / "algs" / "ucs.sh"),
            "astar_euclidean": str(EXPERIMENT_DIR / "algs" / "astar_euclidean.sh"),
            "astar_manhattan": str(EXPERIMENT_DIR / "algs" / "astar_manhattan.sh"),
        },
        "tasks": EXPERIMENT_DIR / ".." / "layouts/*Maze.lay",
    },
    {
        "name": "corners",
        "algorithms": {
            "ucs": str(EXPERIMENT_DIR / "algs" / "ucs_corners.sh"),
            "astar": str(EXPERIMENT_DIR / "algs" / "astar_corners.sh"),
        },
        "tasks": EXPERIMENT_DIR / ".." / "layouts/*Corners.lay",
    },
    {
        "name": "food",
        "algorithms": {
            "ucs": str(EXPERIMENT_DIR / "algs" / "ucs_food.sh"),
            "astar": str(EXPERIMENT_DIR / "algs" / "astar_food.sh"),
        },
        "tasks": EXPERIMENT_DIR / ".." / "layouts/*Search.lay",
    },
]

SUBMITTER = EXPERIMENT_DIR / "submit_tsp.sh"
RUNSOLVER = EXPERIMENT_DIR / "runsolver"


if __name__ == "__main__":
    for experiment in experiments:
        runner = RunningScenario(
            solvers=experiment["algorithms"],
            tasks=str(experiment["tasks"].resolve()),
            submit_file=SUBMITTER,
            constraints=ExecutionConstraints(
                s_wall_time=30, s_real_memory="1G", enforcer=RunSolver(RUNSOLVER)
            ),
        )
        scenario_path = EXPERIMENT_DIR / f"scenario-{experiment['name']}"
        runner.generate_scenario(scenario_path)
