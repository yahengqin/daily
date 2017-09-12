from apscheduler.schedulers.blocking import BlockingScheduler
from daily.work.bingpage import BingPage


def bing_page_task():
    print("fuck shit python")
    bing_page = BingPage()
    bing_page.load()
    print("fuck shit python")


def start():
    task_scheduler = BlockingScheduler()
    # 添加定时任务执行Bing背景图下载任务
    task_scheduler.add_job(bing_page_task, 'cron', day_of_week="0-6", id='bing_page_load')
    task_scheduler.start()
