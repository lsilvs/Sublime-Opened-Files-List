import sublime,sublime_plugin,os

class OpenedFilesListCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        window = sublime.active_window()
        views = window.views()
        f = open('/tmp/subl_opened_files', 'w')

        fileNames = ''
        for view in views:
            if view and view.file_name():
                f.write(view.file_name().replace(" ", "\ ") + '\n')

        f.close()
        window.run_command('close_all')
