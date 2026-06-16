# classifies protocol validation failures for diagnostics


class ProtocolFailureClassifier:

    # classifies one failure message
    def classify_failure(self, failure_message: str) -> str:
        message = failure_message.lower()

        if "timeout" in message:
            return "timeout_failure"

        if "crc" in message or "checksum" in message:
            return "integrity_failure"

        if "sequence" in message or "order" in message:
            return "ordering_failure"

        if "oversized" in message or "size" in message:
            return "frame_size_failure"

        if "disconnect" in message or "connection" in message:
            return "connection_failure"

        if "address" in message:
            return "address_failure"

        if "unknown id" in message or "unexpected id" in message:
            return "identifier_failure"

        return "unknown_failure"

    # classifies multiple failure messages
    def classify_failures(self, failure_messages: list[str]) -> list[dict]:
        return [
            {
                "message": message,
                "category": self.classify_failure(message),
            }
            for message in failure_messages
        ]