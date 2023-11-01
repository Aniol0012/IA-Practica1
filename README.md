# IA-Practica-1

## Description
This repository is made to develop some implementations of search algorithms for PacMan game. This implementations can be found in [search.py](search/search.py).
The heuristics implementation can be found in [searchAgents.py](search/searchAgents.py) file. <br>
You can also check the [report](report.pdf) made for more information.

# Requirements

The requirements can be found in [requirements.txt](requirements.txt) file. But you can also install it manually:

```shell
sudo apt install expect task-spooler
```
````shell
sudo apt install python3-pandas
````

````shell
sudo apt install pip
````

````shell
pip3 install optilog
````
Note: If optilog is not working, try to reboot.

## Run

To run this project go to the [search](search) directory:

````shell
cd search/
````

And then give permissions to all shell scripts:

````shell
chmod +x experiment/runsolver experiment/*.sh experiment/algs/*.sh
````

Then run the experiment:

````shell
optilog-runnig experiment/scenario-search submit
````
Note: If this command is done more than 1 time, add `--overwrite` at the end of the previous command.

````shell
tsp
````

You can also run the [experiment.py](search/experiment/experiment.py) file:

````shell
python3 experiment/experiment.py
````

Note: All the system path to [search](search) directory must not contain any spaces at all, otherwise the project might not work.

## Run heuristics
To run the implemented heuristics `cornersHeuristic` and `foodHeuristic` can be done with these commands:

- **cornersHeuristic**:
```shell
python3 pacman.py -l <layout> -p AStarCornersAgent -z 0.5
```

- **foodHeuristic**:
````shell
python3 pacman.py -l <layout> -p AStarFoodSearchAgent
````

## Layouts

All the layouts can be found in [layouts](search/layouts) directory.
To generate new layouts you can use this [map generator](https://github.com/jponf/Pacman-Project-Search-MapGen) tool.

## Authors
- [Aniol Serrano Ortega](https://github.com/Aniol0012)
- [Aleix Segura Paz](https://github.com/aleixsegura)