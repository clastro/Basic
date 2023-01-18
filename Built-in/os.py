elapsed_time = 2/60
os.system("slackbot -d '@id' -m 'complete AFib with %f minuates '"%elapsed_time)

# Change Current Directory
os.chdir("/smc_work/datanvme/smc/origin/")

# path for import package
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["PYTHONPATH"] = parent_dir + ":" + os.environ.get("PYTHONPATH", "")
