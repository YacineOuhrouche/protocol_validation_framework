# validates simple packet checksums for protocol integrity testing


class ChecksumValidator:

    # calculates an 8-bit additive checksum
    def calculate_checksum(self, data: bytes) -> int:
        return sum(data) & 0xFF

    # validates data against an expected checksum
    def validate_checksum(self, data: bytes, expected_checksum: int) -> bool:
        calculated_checksum = self.calculate_checksum(data)

        return calculated_checksum == expected_checksum