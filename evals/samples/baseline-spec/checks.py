from scheduler import available

bookings = [{"room": "room-a", "start": 10, "end": 20}]
assert available(bookings, "room-a", 20, 30), "adjacent later interval must be accepted"
assert available(bookings, "room-a", 0, 10), (
    "adjacent earlier interval must be accepted"
)
assert not available(bookings, "room-a", 19, 30), "real overlap must be rejected"
assert not available(bookings, "room-a", 12, 15), "contained interval must be rejected"
assert available(bookings, "room-b", 12, 15), "separate rooms must remain independent"
print("5 existing scheduling checks passed")
