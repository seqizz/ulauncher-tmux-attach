from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction
import os

class PassExtension(Extension):

    def __init__(self):
        super(PassExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        pipe = os.popen("if tmux ls > /dev/null 2>&1; then tmux ls; else echo none; fi")
        terminal_binary = extension.preferences['terminal_binary']
        console_parameters_attach = extension.preferences['console_parameters_attach']
        console_parameters_new = extension.preferences['console_parameters_new']
        output = pipe.read()
        if output.splitlines()[0] != "none":
            for line in output.splitlines():
                items.append(
                    ExtensionResultItem(
                        icon='images/tmux.png',
                        name='Attach session %s' % line.split(' ')[0],
                        description=line,
                        on_enter=RunScriptAction(terminal_binary + ' ' + console_parameters_attach % line.split(' ')[0], None)
                    )
                )
        else:
            items.append(
                ExtensionResultItem(
                    icon='images/tmux.png',
                    name='Create a new tmux session',
                    description='No active tmux sessions found',
                    on_enter=RunScriptAction(terminal_binary + ' ' + console_parameters_new, None)
                )
            )

        return RenderResultListAction(items)

if __name__ == '__main__':
    PassExtension().run()
