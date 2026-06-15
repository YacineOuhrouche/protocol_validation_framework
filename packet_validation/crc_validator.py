# validates crc-16 checksums for packet integrity testing


class CrcValidator:

    # calculates crc-16-ccitt for packet data
    def calculate_crc16(self, data: bytes, initial_value: int = 0xFFFF) -> int:
        crc = initial_value

        for byte in data:
            crc ^= byte << 8

            for _ in range(8):
                if crc & 0x8000:
                    crc = (crc << 1) ^ 0x1021
                else:
                    crc <<= 1

                crc &= 0xFFFF

        return crc

    # validates data against an expected crc-16 value
    def validate_crc16(self, data: bytes, expected_crc: int) -> bool:
        calculated_crc = self.calculate_crc16(data)

        return calculated_crc == expected_crc