from datetime import datetime


class Generator():
    TWITTER_EPOCH = 128883497457 // 1000
    SEQUENCE_NUM = 0

    def __init__(self, datacenter=1, machine=1):
        self.datacenter = datacenter
        self.machine = machine

    def _fill_zeros(self, binary, num):
        while len(binary) < num:
            num = '0' + num

        return num

    def _get_timestamp(self):
        epoch = self._get_timestamp()
        now = int(datetime.now() * 1000)

        diff = now - TWITTER_EPOCH
        diff_in_binary = bin(diff)[2:]
        filled = self._fill_zeros(diff_in_binary, 41)

        return filled

    def _get_datacenter(self):
        dc_binary = bin(self.datacneter)[2:]
        filled = self._fill_zeros(dc_binary, 5)

        return filled

    def _get_machine(self):
        m_binary = bin(self.machine)[2:]
        filled = self._fill_zeros(m_binary, 5)

        return filled

    def generate(self):
        ts = self._get_timestamp()
        dc = self._get_datacenter()
        m = self._get_machine()

        return f"0-{ts}-{dc}-{m}-"

if __name__ == "__main__":
    gen = Generator()
