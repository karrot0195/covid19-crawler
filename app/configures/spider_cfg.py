import schedule
import time
import os

class SpiderConfigurator():
    path='covid19_spider.py'
    is_enabled=True

    def __init__(self, options):
        print('initial spider')
        self.exec_time=options.time_exec

    def run(self):
        print('Scheduler initialised')
        schedule.every(self.exec_time).minutes.do(lambda: os.system('scrapy runspider ' + self.path))
        print('Next job is set to run at: ' + str(schedule.next_run()))
        while True:
            if self.is_enabled is False:
                break
            schedule.run_pending()
            time.sleep(1)

            
    def stop(self):
        self.is_enabled = False