from datetime import timedelta


from subframes.subframe1 import create_subframe1
from subframes.subframe2 import create_subframe2
from subframes.subframe3 import create_subframe3
from subframes.subframe4_special_messages import create_subframe4_special_messages
from subframes.subframe4_nmct import create_subframe4_nmct
from subframes.subframe4_sv_health import create_subframe4_sv_health
from subframes.subframe4_reserved import create_subframe4_reserved
from subframes.subframe4_sv import create_subframe4_sv
from subframes.subframe5_sv import create_subframe5_sv
from subframes.subframe5_sv_health import create_subframe5_sv_health

class GpsMessage:
    def __init__(self, start_date):
        self.start_date = start_date
        self.frames = [ self.get_subframes(page) for page in range(1, 26) ]

    def get_subframes(self, page):
        subframes = []
        date = self.start_date + timedelta(seconds=30 * (page - 1))

        subframes.append(create_subframe1(date))
        subframes.append(create_subframe2(date + timedelta(seconds=6)))
        subframes.append(create_subframe3(date + timedelta(seconds=12)))

        if page in [1, 6, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24]:
            subframes.append(create_subframe4_reserved(date + timedelta(seconds=18)))
        elif page >= 2 and page <= 10:
            subframes.append(create_subframe4_sv(page, date + timedelta(seconds=18)))
        elif page == 13:
            subframes.append(create_subframe4_nmct(date + timedelta(seconds=18)))
        elif page == 17:
            subframes.append(create_subframe4_special_messages(page, date + timedelta(seconds=18)))
        elif page == 25:
            subframes.append(create_subframe4_sv_health(date + timedelta(seconds=18)))

        if page >= 1 and page <= 24:
            subframes.append(create_subframe5_sv(page, date + timedelta(seconds=24)))
        else:
            subframes.append(create_subframe5_sv_health(page, date + timedelta(seconds=24)))

        return subframes

    def __str__(self):
        return '\n\n'.join([str(subframe) for subframes in self.frames for subframe in subframes])
