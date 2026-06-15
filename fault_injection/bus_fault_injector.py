# simulates bus-level communication faults for protocol robustness testing


class BusFaultInjector:

    # creates the bus fault injector
    def __init__(self):
        self.disconnected = False
        self.contention_active = False
        self.noise_active = False

    # simulates a device disconnect
    def disconnect_bus(self) -> None:
        self.disconnected = True

    # clears a simulated device disconnect
    def reconnect_bus(self) -> None:
        self.disconnected = False

    # simulates bus contention
    def enable_contention(self) -> None:
        self.contention_active = True

    # clears bus contention
    def disable_contention(self) -> None:
        self.contention_active = False

    # simulates bus noise
    def enable_noise(self) -> None:
        self.noise_active = True

    # clears bus noise
    def disable_noise(self) -> None:
        self.noise_active = False

    # returns whether any bus fault is active
    def has_active_fault(self) -> bool:
        return self.disconnected or self.contention_active or self.noise_active