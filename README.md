# docker compose python runner (template)
- main.py main program, can run independently i.e. in windows, reads infos from secrets.yml and hardcoded variables.
- run_env.py run (within docker to provide .env valuues) and call main.py but use environment values.

## features
- run_env.py reads configured .env parameters and loads them into main.core_program()
- main.py simply runs the main program with hardcoded parameters
- Dockerfile satisfies requirements.txt
- optional debug

# todo (when needed)
- loop the program? or depend on restart?
- cronjobs?