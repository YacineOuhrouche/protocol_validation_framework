# tests protocol failure classification behavior

from diagnostics.protocol_failure_classifier import ProtocolFailureClassifier


# verifies that timeout failures are classified
def test_failure_classifier_detects_timeout():
    classifier = ProtocolFailureClassifier()

    result = classifier.classify_failure("uart timeout while waiting")

    assert result == "timeout_failure"


# verifies that integrity failures are classified
def test_failure_classifier_detects_integrity_failure():
    classifier = ProtocolFailureClassifier()

    result = classifier.classify_failure("crc mismatch detected")

    assert result == "integrity_failure"


# verifies that ordering failures are classified
def test_failure_classifier_detects_ordering_failure():
    classifier = ProtocolFailureClassifier()

    result = classifier.classify_failure("sequence id mismatch")

    assert result == "ordering_failure"


# verifies that frame size failures are classified
def test_failure_classifier_detects_frame_size_failure():
    classifier = ProtocolFailureClassifier()

    result = classifier.classify_failure("packet size exceeded")

    assert result == "frame_size_failure"


# verifies that connection failures are classified
def test_failure_classifier_detects_connection_failure():
    classifier = ProtocolFailureClassifier()

    result = classifier.classify_failure("device disconnected")

    assert result == "connection_failure"


# verifies that unknown failures are classified
def test_failure_classifier_detects_unknown_failure():
    classifier = ProtocolFailureClassifier()

    result = classifier.classify_failure("random failure")

    assert result == "unknown_failure"


# verifies that multiple failures can be classified
def test_failure_classifier_classifies_multiple_failures():
    classifier = ProtocolFailureClassifier()

    results = classifier.classify_failures(
        [
            "uart timeout while waiting",
            "crc mismatch detected",
        ]
    )

    assert len(results) == 2
    assert results[0]["category"] == "timeout_failure"
    assert results[1]["category"] == "integrity_failure"