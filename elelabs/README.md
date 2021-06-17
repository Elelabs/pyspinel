# Elelabs Pyspinel vendor commands and properties


## Quick start

The spinel-cli tool provides an intuitive command line interface, including all the standard OpenThread CLI commands, plus full history accessible by pressing the up/down keys, or searchable via ^R. There are a few commands that spinel-cli provides as well that aren't part of the standard set documented in the command reference section.

Connect the **Elelabs ELEstick** USB Adapter or **Elelabs ELEshield** Raspberry Pi Shield to your computer or Raspberry Pi.
Locate the product serial port. (For Windows it will be *COM1*, *COM2*, etc. For Linux it will be */dev/ttyS1*, */dev/ttyS2*, etc.)

Then run the Pyspinel CLI, using the path to your simulated build:

```
$ cd <path-to-pyspinel>
$ spinel-cli.py -u /dev/ttyS1 -b 115200 --vendor-path=elelabs
spinel-cli > version
SL-OPENTHREAD/1.1.2.0_GitHub-5c2ad91cf; EFR32; Jun 16 2021 22:54:45
Done
spinel-cli > vendor data
Elelabs
Done
ELU013
Done
spinel-cli > vendor btl
spinel-cli > exit
```

### Elelabs Thread Spinel Properties

| NUMBER | PROPERTY           | TYPE      | ENCODING | DESCRIPTION                                        |
| ------ | ------------------ | --------- | -------- | -------------------------------------------------- |
| 0x3C00 | MFG_CUSTOM_VERSION | Read-Only |    "i"   | (EZSP token) Custom version (**1**)                |
| 0x3C01 | MFG_STRING         | Read-Only |    "U"   | (EZSP token) Manufacturing string (**Elelabs**)    |
| 0x3C02 | MFG_BOARD_NAME     | Read-Only |    "U"   | (EZSP token) Board name (**ELU012/ELU013/ELU014**) |

### Elelabs Thread Spinel Commands

| NUMBER | COMMAND               | DESCRIPTION                                                                                         |
| ------ | --------------------- | --------------------------------------------------------------------------------------------------- |
| 0x3C00 | MFG_LAUNCH_BOOTLOADER | Launch Bootloader NCP command. Causes the NCP to perform a software reset and enter XMODEM bootloader mode |


### Elelabs Pyspinel vendor package commands

The vendor package adds several vendor-specific pyspinel commands. Use the help command to list them all.

#### help

Display detailed help to list all Elelabs vendor commands.

```
spinel-cli > vendor help
Available vendor commands:
==============================================
help  data  btl
```

#### data

Request the value of the *MFG_STRING* and *MFG_BOARD_NAME* properties and display them
Display detailed help on a specific command.

```
spinel-cli > vendor data
Elelabs
Done
ELU013
Done
```

#### btl

Launch Bootloader NCP command. Causes the NCP to perform a software reset and enter XMODEM bootloader mode
Sends the *MFG_LAUNCH_BOOTLOADER* command
```
spinel-cli > vendor btl
```
