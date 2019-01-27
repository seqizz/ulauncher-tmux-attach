Another hacky extension for the [ulauncher](https://ulauncher.io/), this time for Tmux.

It searches your open sessions and attaches to them.

If no sessions found, you can create new one.

This extension uses gnome-terminal by default. If your terminal emulator is different, you should check and edit the parameters in settings.

For example, to be able to use this with KDE Konsole, set following parameters under settings:

- Terminal: konsole
- Attach parameters: --new-tab -e 'tmux att -t %s'
- New session parameters: --new-tab -e 'tmux'


![extension screenshot](https://i.imgur.com/U0nUGlZ.png)
