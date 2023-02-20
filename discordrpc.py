import pypresence, time
from pypresence import Presence

client_id = "" ## Your Client ID goes here. Create one at discord.com/developers.
RichPresence = Presence(client_id)

RichPresence.connect()

RichPresence.update(
    state = 'Check out my GitHub page!', ## Text Shown on your profile activity.
    large_image = 'logo', ## The large image to show.
    buttons = [{'label': 'Link to GitHub', 'url': 'https://github.com/r1zopoulxs/'}] ## A button that will open a link.
)

print('Discord Rich Presence is now updated.') ## This will print out the Rich Presence to the terminal.

while True:
    time.sleep(60)