import datetime


def _get_hours():
    """ Получение 24 часа """
    hours = []
    for i in range(24):
        hours.append(i)
    return hours


def _get_minutes():
    """ Получение 60ть минут с интервалом через пять минут """
    minutes = []
    for k in range(0, 60, 5):
        minutes.append(k)
    return minutes


def _get_alarm_finish_date_time(self):
    """ Функция оповещения срока выполнения задачи """
    now_date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if now_date_time == self.finish_date_time:
        message = 'Наступила дата задачи {}'.format(self.task)
        return message