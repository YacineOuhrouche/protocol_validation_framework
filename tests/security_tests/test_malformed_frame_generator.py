# tests malformed frame generation behavior

from security.malformed_frame_generator import (
    MalformedFrameGenerator,
)


# verifies that an empty frame can be generated
def test_create_empty_frame():
    generator = MalformedFrameGenerator()

    frame = generator.create_empty_frame()

    assert frame.payload == b""


# verifies that an oversized frame can be generated
def test_create_oversized_frame():
    generator = MalformedFrameGenerator()

    frame = generator.create_oversized_frame(300)

    assert frame.size() == 300


# verifies that an invalid start frame can be generated
def test_create_invalid_start_frame():
    generator = MalformedFrameGenerator()

    frame = generator.create_invalid_start_frame()

    assert frame.payload[0] == 0


# verifies that an invalid end frame can be generated
def test_create_invalid_end_frame():
    generator = MalformedFrameGenerator()

    frame = generator.create_invalid_end_frame()

    assert frame.payload[-1] == 0