def available(bookings, room, start, end):
    return not any(
        b["room"] == room and start <= b["end"] and end >= b["start"] for b in bookings
    )
