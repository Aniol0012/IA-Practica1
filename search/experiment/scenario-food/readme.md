Please run optilog-running ./relative/path/to/this/scenario/ in order to perform your desired actions.

Examples:

# Submit all jobs
$ optilog-running path/to/scenario submit

# Submit all instances (overwrite previous logs)
$ optilog-running path/to/scenario submit --overwrite

# Delete execution logs
$ optilog-running path/to/scenario clean

# List all tasks. This will print the task's instance path.
$ optilog-running path/to/scenario list tasks

# List all solvers. This will print the solver's names.
$ optilog-running path/to/scenario list solvers

# List all seeds. This will print the seed's values.
$ optilog-running path/to/scenario list seeds

# Submit a specific job, overwrite the logs and use a different seed
$ optilog-running path/to/scenario submit --overwrite --tasks test1.txt --seeds 64

# Submit a specific job, overwrite the logs and use multiple seeds
$ optilog-running path/to/scenario submit --overwrite --tasks test1.txt --seeds 64,82

# Submit multiple tasks, overwrite the logs and use multiple seeds
$ optilog-running path/to/scenario submit --overwrite --tasks test1.txt,test2.txt --seeds 64,82

# Submit multiple solvers, overwrite the logs
$ optilog-running path/to/scenario submit --overwrite --solvers glucose41,cadical

# Execute locally like it would submit:
$ optilog-running path/to/scenario execute test1.txt 64 glucose41
