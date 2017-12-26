import zope.event.classhandler
import applauncher.kernel
import inject
from pyfcm import FCMNotification


class FCMNotificationBundle(object):
    def __init__(self):
        self.config_mapping = {
            "fcm_notification": {
                "api_key": None
            }
        }

        zope.event.classhandler.handler(applauncher.kernel.InjectorReadyEvent, self.event_listener)
        self.notificator = FCMNotification(api_key="")
        self.injection_bindings = {
            FCMNotification: self.notificator
        }

    def event_listener(self, event):
        config = inject.instance(applauncher.kernel.Configuration).fcm_notification
        self.notificator._FCM_API_KEY = config.api_key
