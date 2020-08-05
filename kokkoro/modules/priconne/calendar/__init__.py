from kokkoro.service import Service
from kokkoro.common_interface import *

sv = Service('pcr-calendar')
cn_official_url = 'https://game.bilibili.com/pcr/#p8'
@sv.on_rex(r'^\*?([日台国bB])服?(日历|日程|日程表)?$')
async def calendar(bot, ev:EventInterface):
    match = ev.get_param().match
    server = match.group(1)
    if server == '台':
        await bot.kkr_send(ev, "不好意思，台服日程表暂不支持┭┮﹏┭┮", at_sender=True)
        return
    elif server == '日':
        region = 'jp'
    elif server in ['国', 'b', 'B']:
        region = 'cn'

    yobot_url = f'https://tools.yobot.win/calender/#{region}'
    msg = f'{server}服日程表\nyobot: {yobot_url}'
    if region == 'cn':
        msg = f'{msg}\nbilibili: {cn_official_url}'
    await bot.kkr_send(ev, msg)