This machine is annoyingly fast. You dont have time to go prepare a coffee
while it boots.  Now, if you are in a rush to write down that wonderful idea
you got at midnight. Press the button  (if you left the machine off). You start
typing instant in your new document.  One feature (and I made it in purpose).
Execute the command :off, and the machine will dissapear from any powered form
instant. There is no prompt -Are you sure? y/N or something like this. You will
discard your drafts inmediatly. Here I assume you have the constant, and
healthy rutine of writing :w your ideas as they come.

# Help:
Try with ":help" for the embedded help. Use j,k to go down/up.

# USB charging:
Just plug any USB-C charger and continue. The machine doesnt reboot if you
connect the charger. It will however light the LED indicator to tell you are
powered by USB. One thing to note: because this feature, if the machine is off
and you decide to charge it, it will charge. But it wont show any light, nor it
will start the machine.

# LED indicator:
The led indicator remains off when you are on battery. But it will still notify with some blinking in some circumstances:
1) When the battery level is below 25% slow blinks every 5 min.
2) When the battery level is below 10% fast blinks every 1 min. Below 7% it will stop blinking, and instead it will popup a message overlay every 30s (that you dismiss on an keypress).
3) When writing to disk.
4) When transfering files via BLE.
5) Two little blinks when booting.

# The splash screen:
When you boot, a splash screen will appear, with the cursor parked at the
bottom. You have started a vi session, with a new file still "unnamed", in
normal mode. To start inserting text just press "i". The splash screen will
dissapear as you type. If you prefer to edit or view a previous file, just
press the menu key, or execute :menu.    

# Note on the power button:
The power button switches ON the machine. What it does is literally reseting
the board, that is essentially driven into deep sleep when powering off the
machine with the command :off (or pressing "P" within the menu).  In order to
prevent accidental resets, the button is dissabled when the machine is running,
and i wont do anything until you bring the machine off. This is done connecting
the switch to the reset pin and a dedicated gpio instead of the ground pin.
When the machine is on, that pin remains high, thus protecting the reset
action.  However, you can still reset while you are in the splash screen. I
left this possibility so I can flash firmware into the board during a fraction
of second, before the machine goes to light sleep and breaks the uart
connection with the usb. You can also play reseting the machine in the splash
to demostrate the booting speed.

# The menu:
The text editor nextVI had a powerful mechanism to list files on a buffer, and
some smart commands to open files also, acting all together as a small
filebrowser. This functionality was removed in favour of a more standalone
menu. The menu's purpose is to allow you list files, enter directories, and do
basic filesysem operations like delete, copy or rename. You can sort files by
date or size in reverse or normal order, or search for files.   
Additionally, the file row has a flag indicator to show wether it has been
synchronized with the phone since last modification (directories are
represented with [+] always). The flags are as follow:
1) \- indicates file not sync, neither marked to be sync (local copy only).
2) \* file marked for sync
3) s file is sync
4) x file is remotely deleted (only local copy).

If a file is remotely deleted, the local copy on the typewriter wont be deleted
when synching, but instead it will be marked as "x". This flag can be changed
again if marked for sync again.

Note on the file rows: there are two columns apart of the flag and file name.
The size and the date. Size is given in words, not in bytes. I found this more
useful. Date (last modification) is formated in a compact way. Similar to the
"-h" option when doing "ls" in a linux shell. It shows time if the mtime is
today. Shows day and month otherwise, if mtime is same year. Past years format
the mtime as dd/MM/YY.   When the file name is too long, it will be truncated
to the column. One can always pan with the 0/$ commands to see the head/tail of
the filename.  

Note on VI quit: In a terminal based vi editor, quiting would bring you to the
terminal. But Typewrt doesn't have terminal, it is just a vi editor. The
quitting commands used in vi, like :q or :wq for example, instead of quiting to
a terminal, they bring you to the menu browser. 

# Text editing and wrapping mechanism
There is an important difference between the original nextVI and this
implementation. The line wrapping.    Because of the small size of the screen,
and the purpose of this machine (writing, not coding), a hard-wrap mechanism is
always active. When you type a long line, the text will flow to the next line,
producing a real line-break in the text file. This is different from the
soft-wrapping in which the line splitting is only visual, while the text
written on file still a very long line.  This decission soft/hard has been a
tough one. Originally I was inclined to the soft wrapping. But that continuos
reformatting of text comes heavy in the cpu. Even scrolling text demands
another reformatting of the lines as they appear on the screen.  There are few
uncomfortable aspects of the hard wrapping however. If you open the text in
another device, it will show the text formatted to 40 col width. Exactly the
same as you see here. This I decided to survive with, as the Typewrt was meant
from start to be a standalone editor/processor, and the text wouldn't need that
much work on a different device. The second aspect was more anoying. If you
decide to insert or remove text in the middle of a hard wrapped line, all the
line-breaks inserted by the mechanism would play against you. You will end up
with many ugly, short chunks of text spreaded over several lines.  To keep it
sleek, I decided to implement my own hard-wrapping mechanism.  The machine now
differenciates between a line break inserted by you (when you hit enter) and a
line break forced by the wrapping mechanism. This is done by adding a hidden,
zero-width character besides the line-break character.   When you modify the
content of a previous line, the wrapping mechanism will reformat the line, but
removing those old, forced line-breaks before, so the text will flow gracefuly
again after you escape.  I find this very rewarding, because the text is kept
tidy with very little cpu processing.   

# Keymap and language:
The nextVI editor is very powerful. It allows to change between keyboard
layouts on the fly. I introduced more keymaps and mapped to a dedicated key in
the keyboard, the Alt key. Pressing Alt-e would change to english, Alt-s to
spanish, etc. Pressing Alt-space pops a helper showing the current layout, so
you can find those characters you dont remember.   \ Note on the keyboard: The
keyboard has been fully reimplemented for this machine. Compared to the
original code, Typewrt doesn't run on a terminal at the end of the day. Nor it
has a standard keyboard event handler (it is fully new). The keyboard layout
works mostly with only two layers: normal, and shift (plus dead keys depending
on the language). That means that some characters in some languages, those
accessed with Alt-, are missing. Fortunately those are mostly standard symbols
or parenthesis/brackets, that are very easily accesible throw the english
keyboard.  

Notes on VI editor:  One thing to note is that the language layout affects
mostly to the insert mode, while the normal mode works with the US layout. That
is done in purpose, for muscle-memory of the commands.   


# VI related keys on keyboard:
The Typewrt has a 60% keyboard layout, with 62 keys. On the bottom row it has
the space, Ctrl, Alt and two other types of key: the Cmd key (left and right)
and the Sys/Menu key (on the right). They Sys key brings you to the menu. The
Cmd key has several purposes depending on which VI mode are you. In insert
mode, it lets you parse a normal mode command, returning to the insert mode
after. Think on, "gg" for going to line 0, or "0" to go to start of line...when
you need a quick navigation instruction without leaving insert mode, or you
need to delete some words or lines quick. In normal mode, it just scrolls. Same
as Ctrl-F , but keeping the curor line constant. Also, Ctrl-Cmd scrolls the
other way. 

# Buffers and simultaneously open files:

In VI, a open file is stored in a buffer, that you manipulate. The file doesn't
change until you write the buffer. This buffers are nothing special to VI, as
all text editors work with the same principle. The importance of the word
"buffer" in VI comes with the way you interact with the buffers. You can copy
between them, navigate between them. The copied text can be send to a buffer.
Typewrt has a very limited ram and therefore a special care has been taken when
opening buffers or manipulating them. When the system pass some memory
threshold, it will eventually close buffers that are not modified. It will also
prevent you to open new files into buffer over some quote of memory used.  

# Global marks:

In VI, and nextVI, a very useful feature is the mark. You can tag a cursor
position with a mark flag, a letter. You do so in normal mode pressing
"m+<letter>". At any point you can navigate to that mark pressing
'<letter>Alphabetical marks are buffer-wise. Numerical marks are global, so you
can navigate to that position, in that file, from another file.  In Typewrt the
global marks are persistent. So if you switch on the machine, you can still
navigate to that position in that file, provided you remember the marks you
did. If you dont remember, the command :gmarks prints a list of the marks, and
let you chose one to go to.  

# Notable VI feautures worth mentioning:
Autocompletion, registers, marks, global marks, visual mode. Just play with this.

# Note on the display font:
The Sharp display is amazingly simple to drive. There are just two mainly
primitives: clear, and write. Because displaying a bitmap font is not worth
using a entire library. I just created the few functions I would use as a small
API: writing a line of text, clear the display, and rendering some graphics.
Clear display is one single instruction. The graphics is simply writing the
corresponding lines, everithing at pixel level.  The only interesting part is
the character rendering. For that, a bitmap font is just rendered. Because the
font is a VGA 8x16, 16 lines of the display need to be refreshed everytime a
character appears. This is because the Sharp partial refresh is line-wise.  The
bitmaps for the font glyphs have been stored bit-reversed, because the spi
protocol writes pixels from left to right, while the font bitmaps contain the
gliphs from LSB to MSB. This saves some redundant processing. 

# The font:
I found this font extremely pleasant. It is based in the original VGA font from
IBM (I guess), but slightly reformulated and extended by the ZAP group
Australia.  They have put lot of attention in some characters. Also, the
version used here, with 256 glyphs, covers almost all the european languages.
This group has released as well a 512 character set. But I found this 256 good
enough for my language spectrum.
The font is solid, bold, and renders very nicely. They have created also a
light, modern font. But I still prefer the readability of this one.

# Wireless communication:
The ESP32s3 comes with both wifi and bluetooth. The reason I chose BLE for
remote transfers is power consumption, memory used in the stack and in the
flash, and also because of the avalaibility.  Wifi consumes way more power, and
have way more overhead. But its transmission is much faster. This means that,
from some transfer size up, wifi becomes favorable. The estimate would be
around 0.5 MB. But this would only be favorable if you perform a single
transfer.  If you were transmitting periodically, the time spent with the
antenna on wont be that favorable any longer.  Apart of the power, BLE allows
you to transfer your data to your phone withoutincurring in a public or private
network. You dont need to rely on the wifi signal. The transfer is just between
Typewrt and your phone, with no intermediates. And I love that feature.

# SD card and RTC:
There is a small, feather format, extra board which consists on a RTC and a
micro SD card slot. It is called Adafruit adalogger, and it suits Typewrt2
perfectly. The RTC keeps time and date with an coin cell, and the SD cards is
basically the storage for the mahine.  Regading the SD. Many people would
probably like a slot in the enclosure, so one can extract the card and copy
files. My modern laptop doesnt have SD card slot. I decided to buy a efficient
card reader to transfer photos from my digital camera (beware, bad quality ones
get very hot). The modern version of my camera now transfers all the photos via
wifi!  Somehow I though, the less te card is extracted and inserted, the
better. I want the SD card to seat fixed in the body and act as a hard drive,
with the less possibles chances to fail.  The reason I chose a SD card slot
instead of a soldered EMMC solution is another one: SD cards consume much less
power! they have internal sleep modes, and require less pins as well. Of
course, the SD card writing/reading speeds are much slower than EMMCs, and
that's totally fine for a typewriter who deals with small text files and no
high resolution photos or videos.

For the SD card, I chose an industrial APT single cell card. They are extremely
expensive and come with much less memory, but they are the toughest and more
reliable cards. For the price of a good quality Samsung 64GB, I got this single
cell card with 512 MB. I just loved it.

