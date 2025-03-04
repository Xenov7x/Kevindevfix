from bot import Bot
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from bot.utils import process_delete_schedule

if __name__ == "__main__":
    os.makedirs("downloads", exist_ok=True)
    sc = AsyncIOScheduler()
    sc.start()
    app = Bot()
    app.sc = sc
    sc.add_job(
        process_delete_schedule,
        "date",
        run_date=datetime.now() + timedelta(seconds=5),
        args=(app,),
        max_instances=1,
        id="delete_schedule",
    )
    app.run()
