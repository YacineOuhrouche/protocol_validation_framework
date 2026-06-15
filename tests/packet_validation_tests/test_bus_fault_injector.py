# tests bus fault injection behavior

from fault_injection.bus_fault_injector import BusFaultInjector


# verifies that bus disconnect can be enabled and cleared
def test_bus_fault_injector_disconnect_reconnect():
    injector = BusFaultInjector()

    injector.disconnect_bus()

    assert injector.disconnected is True
    assert injector.has_active_fault() is True

    injector.reconnect_bus()

    assert injector.disconnected is False
    assert injector.has_active_fault() is False


# verifies that bus contention can be enabled and cleared
def test_bus_fault_injector_contention():
    injector = BusFaultInjector()

    injector.enable_contention()

    assert injector.contention_active is True
    assert injector.has_active_fault() is True

    injector.disable_contention()

    assert injector.contention_active is False
    assert injector.has_active_fault() is False


# verifies that bus noise can be enabled and cleared
def test_bus_fault_injector_noise():
    injector = BusFaultInjector()

    injector.enable_noise()

    assert injector.noise_active is True
    assert injector.has_active_fault() is True

    injector.disable_noise()

    assert injector.noise_active is False
    assert injector.has_active_fault() is False