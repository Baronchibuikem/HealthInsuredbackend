#********************
#python imports
#********************
import datetime

import pytz

from django.conf import settings

def get_now_with_sys_timezone():
	dt=datetime.datetime.now()
	tz=pytz.timezone(settings.TIME_ZONE)
	dtz=tz.localize(dt)

	return dtz