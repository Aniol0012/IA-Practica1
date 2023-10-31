#!/usr/bin/env python3

# THIS FILE HAS BEEN AUTOMATICALLY GENERATED
# DO NOT MODIFY IT
import sys
import os
from optilog.abstractscenario import abstract_scenario_entrypoint, AbstractScenarioContext
from pathlib import Path
original_wd = os.getcwd()
scenario_dir = Path(__file__).parent.resolve()

def main():
    context = AbstractScenarioContext(original_wd, scenario_dir)
    abstract_scenario_entrypoint(context)

if __name__ == '__main__':
    main()
