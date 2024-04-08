from gps_message import GpsMessage

def validate_alarm_indications(gps_message: GpsMessage):
    for i, frame in enumerate(gps_message.frames):
        iodc = frame[0].word8.issue_of_data_clock
        iode_1 = frame[1].word3.issue_of_data_ephemeris
        iode_2 = frame[2].word10.issue_of_data_ephemeris

        if iodc != iode_1 or iodc != iode_2:
            return False

        if i % 5 == 3 or i % 5 == 4:
            continue

        frame_content = '\n'.join([str(subframe) for subframe in frame])
        frame_content = ''.join(frame_content.split('\n')[2:10])

        if all([bit == '0' for bit in frame_content]):
            return False

        if all([bit == '1' for bit in frame_content]):
            return False

        if frame_content[:-2] == '10' * 119:
            return False

        for subframe in frame:
            if subframe.word1.preamble != [1, 0, 0, 0, 1, 0, 1, 1]:
                return False

    return True