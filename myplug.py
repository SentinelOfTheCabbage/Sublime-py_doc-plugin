# import sublime
# from sublime import active_window
# import sublime_plugin
# import pickle
# import json
import replacer as sublime_plugin
import os

plugin_folder = r'C:\Users\Tom\AppData\Roaming\Sublime Text 3\Packages\User'
filename = 'myplug.py'

# class ExampleCommand(sublime_plugin.TextCommand, sublime.Window, sublime.View):
class ExampleCommand(sublime_plugin.TextCommand, sublime_plugin.Window, sublime_plugin.View):

    def run(self, edit):
        print(self.view.view_id)
        # print(dir(edit))
        W = active_window()
        V = W.active_view()
        dot = V.viewport_position()
        with open(plugin_folder+'\\x.txt','w') as file:
            file.write(str(dot))
        R = Region
        # print(W.window_id)
        # print(W.active_view().window().window_id)
        # self.view.insert(edit, 0, "Hello, World!")
        # print(dir(sublime_plugin),sublime_plugin.__file__)


if __name__ == '__main__':
    print(__name__)
    with open(filename, 'r') as file:
        current_code = file.read()
    current_code = current_code.replace('import', 'import')
    current_code = current_code.replace(
        'import replacer as sublime_plugin\n', '')

    with open('{}\\{}'.format(plugin_folder, filename), 'w') as file:
        file.write(current_code)
    print('File were updated!')
    print('Write "view.run_command(\'example\')" in console to run it =)')
