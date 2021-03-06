# @date 2018-08-25
# @author Frederic SCHERMA
# @license Copyright (c) 2018 Dream Overflow
# Service base class

import threading

from importlib import import_module

from notifier.notifier import Notifier
from notifier.notifiable import Notifiable
from notifier.signal import Signal

from terminal.terminal import Terminal

from notifier.signal import Signal
from config import config, appliance


class Service(Notifiable):
	"""
	Base class for any service.
	"""

	def __init__(self, name, options):
		super().__init__(name)

		self._notifier = Notifier(self)
		self._mutex = threading.Lock()

	def lock(self, blocking=True, timeout=-1):
		self._mutex.acquire(blocking, timeout)

	def unlock(self):
		self._mutex.release()

	def start(self, data):
		pass

	def terminate(self, data):
		pass

	def sync(self):
		pass

	def notify(self, signal_type, source_name, signal_data):
		pass

	def add_listener(self, notifiable):
		self.lock()
		self._notifier.add_listener(notifiable)
		self.unlock()

	def remove_listener(self, notifiable):
		self.lock()
		self._notifier.remove_listener(notifiable)
		self.unlock()

	def command(self, command_type, data):
		pass

	def receiver(self, signal):
		pass

	def ping(self):
		pass
