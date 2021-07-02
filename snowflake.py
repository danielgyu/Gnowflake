import sys
from datetime import datetime


class Generator():
    TWITTER_EPOCH = 128883497457 // 1000
    SEQUENCE_NUM = 0

    def __init__(self, datacenter: int=1, machine: int=1):
        self.datacenter = datacenter
        self.machine = machine

    def _fill_zeros(self, binary: str, num: int):
        while len(binary) < num:
            binary = '0' + binary

        return binary

    def _get_timestamp(self):
        now = int(datetime.now().timestamp() * 1000)

        diff = now - self.TWITTER_EPOCH
        diff_in_binary = bin(diff)[2:]
        filled = self._fill_zeros(diff_in_binary, 41)

        return filled

    def _get_datacenter(self):
        dc_binary = bin(self.datacenter)[2:]
        filled = self._fill_zeros(dc_binary, 5)

        return filled

    def _get_machine(self):
        m_binary = bin(self.machine)[2:]
        filled = self._fill_zeros(m_binary, 5)

        return filled

    def _get_sequence(self):
        filled = self._fill_zeros(str(self.SEQUENCE_NUM), 5)

        return filled

    def generate(self):
        ts = self._get_timestamp()
        dc = self._get_datacenter()
        m = self._get_machine()
        s = self._get_sequence()
        
        unique_id = f"0-{ts}-{dc}-{m}-{s}"
        self.SEQUENCE_NUM += 1

        return unique_id


def main(datacenter=None, machine=None):
    gen = Generator()

    running = 1
    start = datetime.now()
    while running:
        num = int(input("How many IDs?(default=1, exit=0): "))
        
        if num:
            for _ in range(num):
                print(gen.generate())
        elif num == 0:
            running = 0
        else:
            print(gen.generate())

        if (datetime.now() - start).total_seconds() > 3:
            gen.SEQUENCE_NUM = 0
            start = datetime.now()


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        datacenter, machine = sys.argv[1], sys.argv[2]
        main(datacenter, macine)
    else:
        main()
