![Typewrt2](images/PXL_20260614_162332405.jpg)

# Typewrt Mark II (ver 2.0)

Typewrt is a modern conception of a digital typewriter, designed as an
instrument for creating literary works without the need of further devices or
software. 
The idea revolves around a mechanical feeling, and it is designed with the
following key aspects:
1) Output: A reflective memory-in-pixel monochrome LCD from SHARP. This is a
4.4" display with a todays low resolution (320x240, QVGA). This resolution is 
enough to produce sharp glyphs using VGA font 8x16 bitmaps. It allows for 15
lines with 40 characters. The readability is exceptional both indoors and
outdoors. Because of the resolution and the ability to perform partial
refreshes, it updates very fast. 

2) Input: A mechanical keyboard with high quality switches and thick PBT
keycaps, arranged in a 60% layout. Mounted in a sturdy brass plate and a custom
made PCB. 
4) Power: Typewrt doesn't produce light. It doesn't stress the eyes. It doesn't
produce heat when you write on the lap. And it does not need a charger around.
The SHARP display is ultra low power. As it does the keyboard and the main
board. 
3) Process: The core of the device, and the main departure from a typewriter or 
a simple drafting device. Typewrt is an embedded vi text editor. It allows to
navigate through the document or documents very efficiently. Manipulate text
with any complexity, and recursively. Do search and replace, etc. You can even
autocomplete words, or perform fuzzy searches. 
5) Ergonomics: The design is meant to be robust and stable. The keyboard height
has been minimized. The display distance and viewing angle is kept large enough
to allow long writing sessions. The keyboard has been silenced as much as
possible, so you have a good peace of mind when typing in public places.
The tactility and response of the keyboard is very conforting. 
6) Remote sync: The device has LE Bluetooth and allows to copy your files to
your phone consuming very little, and without needing external networks.

A display that
doesn't produce light or stress your eyes. That works wonderfully on daylight.
A keyboard that exerts mechanical precission and invites to type in. An ultra
low power device that lets you write continuosly for more than two weeks, or
that would hold idle for almost half a year. Typewrt powers on instant into
a blank document. Ready to type. The display doesn't have any lag. Keyboard,
display and processor work all together to produce a fast, responsive and
reliable experience. Without even noticing you are typing on an electronic
device.   Even though, Typewrt lets you transfer your files with Bluetooth to
your phone. That means, you can have a full copy of your text in the phone
without recurring into networks.  A small app in the phone let you commit your
changes into a git repository. A very convenient, fast and secure way of having
your text back up, and allowing you to revert or review changes easily. 

Now, the core of Typewrt is the text editor. It is an embedded version of the
vi clone nextvi. In addition to the powerful editing capabilities, it supports
utf8, and allows to change the language layout on the fly. 

Maybe one of the features I like most is the simplicity. There is no unnecesary
clutter. No shell, no loggings, no passwords, no such a thing like entering in
the editor program. The machine is itself the editor program, and nothing else.
It just lets you, write. There is just one single thing you can do with this
machine.

# Vi at a glance:

Vi is one of the main text editors in unix/linux distributions. Its
functionality is divided into three different modes: insert, nomal and ex mode.
Once you are inside vi, you press "i" to enter insert mode, and you can start
typing in your document. Many people hate vi just because this initial
frustration, akwardness responses of the keyboard when you are not in Insert
mode. This is because vi is very powerful. It has many key bindings, and the
learning curve is somehow  step. 

In insert mode, it behaves like the simplest text editor you could imagine. As
far as you dont escape, pressing the Esc key, you basically insert characters
in your text buffer. There are very few but useful key bindings in insert mode
however. Press Ctrl-W to delete your last word. Or Ctrl-N to autocomplete a
word you started typing.  To save your text (to write your buffer into a file),
you escape to enter normal mode, then you type ":" to enter ex mode, and "w
<filename>" to write.

Normal mode is where things get fun. In this mode you dont create text by
typing, but instead you type keybindings to manipulate the text you already
have, or navigate throw the buffer/buffers, copy or paste pieces of text into
the buffer, or different registers, search or replace, delete, and many other
things. This editor paradigm works very nice for coding, among other things,
were you would spend considerable part of your time rearranging pieces of text
or modifying functions or variables. For writing fiction I find it equally
useful.  The navigation, or movements, are the first step departing from your
standard, plain editor. The left, right, up and down cursor movements in vi are
arranged in the main keyboard row as h,j,k,l for left, down, up and right. If
you get used to this, you wont miss again the arrow keys.  You can move forward
or backwards by words, paragraphs, programmed marks, entire documents/buffers.
You can concatenate actions with movements, like delete 5 words backwards, or
find character <character> 3 times, to say, or copy text til mark <mark>, or
paste register 1...  Pressing "." in normal mode executes the last instruction
again. For example "dB" to delete backwards  to the begining of a word
(including punctuation). Then pressing "." will continue to delete that way.


