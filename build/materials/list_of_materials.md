# Detailed list of materials:
  This is the list for all the components in the buid. It does not contain the
specific components for the PCBs (described in the respective folders), nor the
extra material for the building process (solder wire, flux, sand paper or glue
for the enclosure finish). Some makes like the switches, stabs, keycaps, SD
card, or the keyboard plate material, paint, etc, are just mention for
completeness of the project (feel free to pick your own).

## Display
* Sharp MIP LS044Q7DH01 : 4.4" reflective LCD, SPI protocol with 3.3V logic and
  5.0V power. It does partial refreshes with 1 line granularity. 
* Display PCB : custom made PCB for the Sharp display. It basically exposes the
  MOSI, SCLK and CS pins from the display, links the enable pin to the 3.3V
  input (note that the 3.3V is provided from the secondary LDO2 in the ESP
  board, that can be switched on/off), provides the 5V from the 3.3V with an
  efficient booster, and provides the VCOM signal via an ultra low power timer.
  Materials for the PCB are listed in the PCB folder.
* PC 0.7mm screen protector.

## Keyboard
* Laser cut bronze keyboard plate.
* Switches x62 MX cherry style (Durock silent Shrimp T1, custom lubbed)
* Stabilizers (Durock), pcb mounted, 1.6mm pcb gap.
* Switches foam (between plate and pcb).
* keyboard PCB : arranged the switches in a 8x8 matrix, all switches with 
  diodes, and an octal latch as the only component. Materials for the PCB are
  listed in the PCB folder. 
* Keycaps for MX cherry compatible (PBTFans doble shoot 1.6mm thick)

## Cables

## Hardware
* Feather S3[d] from Unexpected Maker (esp32s3 with 16Mb Flash and 8Mb PSRAM)
* Adafruit adalogger featherwing: RTC with coin cell and SD card slot.
* SD card : ATP 512 Mb (industrial grade, SLC) FAT32 formatted.
* Antenna : Optional (there is space under the display lid to glue one). The
  feather board has both a small antenna and connector for external one.

## Battery
* LiIon 26650 with protection circuit (they are slightly longer, even though the
  design has margin for 5mm difference) : 6000 mAh.

## Enclosure
* Main body, splitted in two parts for 3d printing.
* Display lid, splitted in two parts for 3d printing.
* Display clamps x2, to hold the pcb to the lid.
* Battery holder-container.
* Battery holder-lid.
* Battery contacts, negative and positive.
* Screws: all M2.5. 2x12mm, 5x16mm, 2x5mm and 2x5mm flat head, conical for the
  USB connector.
* Inserts: for M2.5, 3.9mm diameter, 4mm height, 9x.
* Paint, filler and primer : acrylic spray paint. 
* Rubber pads : adhesive, 3M, 10mm diameter, 1mm thick.

## USB connector
* Amphenol USB-C right angle rugged.
* USB PCB : a small breakboard for the connector, exposing the power, gnd, and
  data lines to the board, and pulling down with 5.1k resistors the CC1 and CC2
  lines upstream. It has also a small jumper to cut the dat lines, in case you 
  want to avoid any accident breaking the firmware of the typewriter when
  connecting the USB. Note that the machine is meant to transfer files wireless
  anyhow, and it doesnt grant access to your SD card with the USB.   
* USB-C male connector breakboard, to mate the board with the enclosure
  connector (see also the cables section).

## Led indicator
* Kingbright 1.8mm L-2060YD yellow
* current limiter resistor 320 Ohm

## Power button
* Omrom sealed tactile switch. 8x8mm B3WN.
