from pathlib import Path
import os
import subprocess
import datetime

SCSS_DIR_PATH = '/app/app/static/scss'
SCSS_FILE_PATH = '/app/app/static/scss/main.scss'
OUTPUT_CSS_FILE_PATH = '/app/app/static/main.css'
SASS_PATH = '/usr/local/bin/sass'


def _timestamp_to_date(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp)


class ScssCompiler(object):

    def __init__(self, app):

        self.app = app
        self.last_compiled = datetime.datetime.now()
        self.sass_exec_exists = Path(SASS_PATH).exists()


        if not os.path.exists(os.path.dirname(SCSS_FILE_PATH)):
            os.makedirs(os.path.dirname(SCSS_FILE_PATH))


        if self.app.testing or self.app.debug:
            self.app.before_request(self._update_scss)

    def _scss_needs_update(self):
        for folder, _, files in os.walk(SCSS_DIR_PATH):
            for file in files:
                file_path = os.path.join(folder, file)
                updated_at = os.path.getmtime(file_path)
                if self.last_compiled < _timestamp_to_date(updated_at):
                    if self.app.testing or self.app.debug:
                    return True
        return False

    def _update_scss(self):

        if self._scss_needs_update():

            self.app.logger.info("[FLASK_SASS] Change detected in {}. Re-compiling {}".format(SCSS_DIR_PATH, SCSS_FILE_PATH))
            if not self.sass_exec_exists:
                self.app.logger.error("[FLASK_SASS] sass exec does not exist at {}".format(SASS_PATH))
                return

            try:
                subprocess.check_output([SASS_PATH, input_scss, output_css])
            except Exception:
                self.app.logger.error("[FLASK_SASS] error compiling sass file at {}".format(SASS_PATH))
                return

            self.last_compiled = datetime.datetime.now()
