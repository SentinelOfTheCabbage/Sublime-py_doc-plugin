# import sublime
# import sublime_plugin
# import pickle
# import json
import replacer as sublime_plugin
import os

plugin_folder = r'C:\Users\Tom\AppData\Roaming\Sublime Text 3\Packages\User'
filename = 'myplug.py'


class ExampleCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        PATH = r'C:\Users\Tom\Documents\Python_projects\SublimePlugin'
        ans = self.get_methods(sublime, 'sublime', 0)
        with open(PATH + r'\sublime.json', 'w') as file:
            file.write(str(ans))

    def get_methods(self, obj: object, parent_obj: str, depth)->():
        content = dir(obj)
        result = {}
        is_module = {}
        is_hash = {}
        is_float = {}
        is_elementary = {}
        bullshit = [
            "<class 'int'>",
            "<class 'float'>",
            "<class 'str'>",
            "<class 'list'>",
            "<class 'dict'>",
            "<class 'set'>",
        ]

        if depth < 2:
            for element in content:
                exec('is_module["key"] = (str(type(' + parent_obj +
                     '.' + element + ')) == "<class \'module\'>")')
                exec('is_float["key"] = (str(type(' + parent_obj +
                     '.' + element + ')) == "<class \'sys.float_info\'>")')
                exec('is_hash["key"] = (str(type(' + parent_obj +
                     '.' + element + ')) == "<class \'sys.hash_info\'>")')
                exec('is_elementary["key"] = str(type(' +
                     parent_obj + '.' + element + ')) in bullshit')

                if not (is_hash['key'] or is_float['key']):
                    if not is_module['key']:
                        exec('result[\'' + element + '\'] = ' +
                             parent_obj + '.' + element)
                    else:
                        print(parent_obj + '.' + element)
                        exec('result[\'' + element + '\'] = ' + 'self.get_methods(' + parent_obj + '.' +
                             element + ', \'' + parent_obj + '.' + element + '\', ' + str(depth + 1) + ')')
                else:
                    continue
        return result

if __name__ == '__main__':
    print(__name__)
    with open(filename, 'r') as file:
        current_code = file.read()
    current_code = current_code.replace('# import', 'import')
    current_code = current_code.replace('import replacer as sublime_plugin\n', '')

    with open('{}\\{}'.format(plugin_folder,filename), 'w') as file:
        file.write(current_code)
    print('File were updated!')
