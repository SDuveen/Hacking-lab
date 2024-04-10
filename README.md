# Hacking-lab

This repository contains code to generate GPS navigation messages that are able to be used to spoof GPS signals.
The signals generated with the code are valid GPS navigation messages with random content.
Currently, it is not supported to input your own data into the GPS navigation messages to spoof the location of a receiver to any location, just to facilitate the misinterpreting of the location.

### Instructions to run

An example of how to generate a GPS navigation message is within `main.py`, where generating a GPS message is as simple as:

```python
gps_message = GpsMessage()
```

or to generate a GPS navigation message at a current moment in time, one only needs to supply a `datetime` object for the `start_date`:

```python
gps_message = GpsMessage(start_date=datetime.now())
```

Furthermore, it is possible to check a GPS message object if it validates all the alarm indications as proposed in the ICD to ensure it will not be flagged by a GPS receiver.
This can be done as follows:

```python
gps_message = GpsMessage(start_date=datetime.now())

if not validate_alarm_indications(gps_message):
    print('Alarm indications are invalid')
else:
    print(gps_message)
```

Printing the gps message will print each subframe of the GPS navigation message, where one word is printed per line. The following is the example output for the last 5 subframes of a GPS navigation message:

```shell
100010110101111011011011001101
010011100010010000000100100100
010000010110111101000010101110
001111011000110111100100010111
001101001011110111011111111111
000001111010100001011010111001
000000110100001111000110001001
000000000011110000100011110011
010101000110011110111011101110
010000010111011110010100010100

100010110101011001100011110101
010011100010011000000100111011
000000001100111110011111101000
010000110000111010101000010110
011011001111011011011111100001
011000000001000101111001101101
111101111011011001000101001010
011011001011011110011011110101
011000111111110101000011101010
001000000000001001111111100001

100010111100100111111100111001
010011100010100000000100100111
001110011100100111010111101000
111001111101001100111000101011
110010000100000111011000001101
000000011001111011001110010100
010101101100101011110001110001
110110000000110100101010011100
010101001110111101001111000001
000000000111010011101100010010

100010110010001000101111001110
010011100010101000000100000111
010110010110111100110000000000
010001101000000011011000110000
111111000000000111101000110100
010000011101011101111010111110
110010111000111001011111100001
011100000101000101000101111010
110000000010010100001101111000
000100011000000100111111000110

100010110100100101000110011110
010011100010110000000100100110
101100110100011001010011011001
001101111111110101110111001011
110100001000001111110010101111
101111000010110000000001001011
100011011111111100010001000000
011101000011011101100011011111
000110100110110111110010001101
111011000000000000000000101011
```

### Explanation of the files

- `alarm_indications.py`: contains a function to check for a GPS navigation message if it follows all the alarm rules.
- `gold_code_generator.py`: contains a function to generate a PRN code for a certain number, used in GPS navigation message transmission
- `gps_message.py`: contains the `GpsMessage` object definition
- `gps_time.py`: contains a function that will calculate the week number and time of week used within each frame of the GPS navigation message.
- `parity_encoding.py`: contains a function to calculate the parity bits for any word within the GPS navigation message based on the parity encoding scheme within the ICD.
- `subframes/subframeX.py`: contains the GPS navigation message's subframe structure for each available subframe.
- `subframes/utils.py`: contains code to make the individual subframe definitions easier.
