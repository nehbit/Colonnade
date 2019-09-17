import sublime
import sublime_plugin

class MakeTwoColumnsCommand(sublime_plugin.WindowCommand):
    def run(self):
        # load the settings to transfer
        res = sublime.load_resource(
            "Packages/Colonnade/TwoCol.sublime-settings")
        my_settings = sublime.decode_value(res)
        # transfer the settings to the user settings
        user_settings = sublime.load_settings("Preferences.sublime-settings")
        for k, v in my_settings.items():
            user_settings.set(k, v)
        # save the user settings
        sublime.save_settings("Preferences.sublime-settings")

class MakeThreeColumnsCommand(sublime_plugin.WindowCommand):
    def run(self):
        # load the settings to transfer
        res = sublime.load_resource(
            "Packages/Colonnade/ThreeCol.sublime-settings")
        my_settings = sublime.decode_value(res)
        # transfer the settings to the user settings
        user_settings = sublime.load_settings("Preferences.sublime-settings")
        for k, v in my_settings.items():
            user_settings.set(k, v)
        # save the user settings
        sublime.save_settings("Preferences.sublime-settings")

class MakeFourColumnsCommand(sublime_plugin.WindowCommand):
    def run(self):
        # load the settings to transfer
        res = sublime.load_resource(
            "Packages/Colonnade/FourCol.sublime-settings")
        my_settings = sublime.decode_value(res)
        # transfer the settings to the user settings
        user_settings = sublime.load_settings("Preferences.sublime-settings")
        for k, v in my_settings.items():
            user_settings.set(k, v)
        # save the user settings
        sublime.save_settings("Preferences.sublime-settings")