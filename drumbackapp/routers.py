from drumbackapp.system_info import broadcast_sys_info
from swampdragon import route_handler
from swampdragon.route_handler import BaseRouter


class SysInfoRouter(BaseRouter):
    route_name = 'sys'

    def get_subscription_channels(self, **kwargs):
        broadcast_sys_info()
        return ['sysinfo']


route_handler.register(SysInfoRouter)