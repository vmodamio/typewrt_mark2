Typewrt keyboard is designed from scratch. From the pcb design to the driver
and communication protocol.  It cannot be called "driver" anymore since the
Mark II, as now everything is embedded in a unique firmware. But the concept
remains the same to my first Typewrt vision. In Typewrt 1, a interrupt driven
microcontroller was sending key events via uart, sleeping the rest of the time.
In typewrt 2, the whole firmware is in the same microcontroller, that is
globally sleeping when no key is pressed.

# Matrix and scaning mechanism:
The 60% ISO keyboard layout has 62 keys. The optimal way to arrange them would
be a 8x8 matrix, with only two spares.  Typewrt 2 has this matrix, and it
allowed me to use a very practical multiplexing mechanism to reduce even
further the number of pins used: an octal latch.  This is a small component
with 8 inputs and 8 outputs. You can program the outputs to be insolated
(latched), or to be seeing the inputs. The rows are connected to the outputs
and the columns to the inputs, so the mechanism goes as folow: you input one
high and rest low. This goes so far symmetrically to rows and cols, as the
output is connected to the input. Then you latch the outputs (insolated from
inputs now), and set the inputs...

# Debounce and denonise:
When a key is pressed, the switch contacts will bounce producing an intermitent
connection during few milliseconds, before it settles down. One standard
procedure for avoiding the misleading behaviour is to wait for a safe time
window, and read the status of the switch after. A typical debounce time is 10
to 20 ms. This delay is negligible and your keyboard is perceived as
instantaneous for you.  With this strategy however, the keyboard is not inmune
to noise in the circuit, that could trigger a false key event because of
residual charges in the line,for example. 
For typewrt 2 I opted for a robust debouncing/denoising strategy: using shift
registers.  The basic idea is that the status of a key is scanned several
times, every one millisecond. When te scan reports 8 consecutive and identical
states, that are different to the previous key status, it reports the key event
and changes the key status to the new value.This is maybe one of the pieces of
this project where I havent spare in power consumption, as it demands slightly
more cpu. But at the same time provides a very robust keyboard response, that
delivers key events as fast as possible.

# Keyboard autorepeat:
I have not implemented key autorepeat in Typewrt. That  means, you cannot hold
the backspace and continue deleting characters, for example. Autorepeat doesn't
introduce any important complexity, but I feel it somehow goes against the
philosophy of this machine.  First, without autorepeat I'm forced to delete or
manipulate text in the way vi is meant for. And second, it avoids high
refreshing rates for the display. Now, the Sharp display is quite fast
refreshing, but I wouldnt play finding the compromise between the fastest
backspace deleting speed and the limit this display could reach.  Seriously,
hitting the backspace to delete the last four or five words is highly
inefficient. The faster you would go, the more chances you wont even land in
the character you want. In vi you just press Ctrl-W and delete one full word at
once, with the cursor in the right place! or in normal mode you hit "dB" for
example, or "d5B" and  you delete 5 words at once. 

# Keyboard event:
This part might not be relevant at all for anyone. But it might serve useful
for understanding the potential of custom modifications for keymaps.  In a
normal keyboard, you wouldn't be able to program the caps-lock to perform
whatever you want, for example...  The keyboard events are 8bits. The MSB
indicates key pressed/released. The next bit is for indicating a modifier key.
When it is 0, the next 6 bits represent up to 64 possible physical switches in
the keyboard. When the 7th bit is 1 (modifier), the 6th bit represent
left/right, in case a modfier key is doubled (like Ctrl, or Alt), and the next
5 bit are mapped for Caps-lock, shift, Ctrl, Cmd and Alt modifiers.

