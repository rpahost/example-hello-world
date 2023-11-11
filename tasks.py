from pathlib import Path

from robocorp import workitems
from robocorp.tasks import get_output_dir, task
from RPA.Excel.Files import Files as Excel

import time

@task
def add_datafield_to_task():
    """ Adds a datafield to the task we are running """

    for item in workitems.inputs:
        time.sleep(10)
        Configuration = item.payload['Configuration']
        Task = item.payload['Task']
        # if not hasattr(Task, 'Data'):
        #     Task['Data'] = {'Message' : Configuration["Message"]}
        # else:
        #     Task['Data']['Message'] = Configuration["Message"]
        if not hasattr(Task, 'Data'):
            Task['Data'] = {'Message' : "Hello World"}
        else:
            Task['Data']['Message'] = "Hello World"
        workitems.outputs.create(Task)