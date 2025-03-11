import sys
import time
import threading

class ThinkingAnimation:
    """Animated thinking indicator for CLI"""

    def __init__(self, message="Thinking"):
        self.message = message
        self.running = False
        self.animation_thread = None

    def start(self):
        self.running = True
        self.animation_thread = threading.Thread(target=self._animate)
        self.animation_thread.daemon = True
        self.animation_thread.start()

    def stop(self):
        self.running = False
        if self.animation_thread:
            self.animation_thread.join()
        sys.stdout.write('\r' + ' ' * (len(self.message) + 10) + '\r')
        sys.stdout.flush()

    def _animate(self):
        dots = 0
        while self.running:
            dots = (dots % 3) + 1
            sys.stdout.write(f'\r{self.message}{"." * dots}{" " * (3 - dots)}')
            sys.stdout.flush()
            time.sleep(0.5)
