from datetime import datetime, timedelta

def calculate_time_left(due_datetime_str):
    """
    Menghitung waktu tersisa dalam format 'XX jam YY menit' tanpa leading zero.
    :param due_datetime_str: String tanggal dan waktu jatuh tempo.
    :return: String dalam format 'XX jam YY menit' atau 'YY menit'.
    """
    formats = ["%Y-%m-%d %I:%M %p", "%Y-%m-%d %H:%M"]  # Format 12 jam dan 24 jam
    for fmt in formats:
        try:
            due_datetime = datetime.strptime(due_datetime_str, fmt)
            break
        except ValueError:
            continue
    else:
        print(f"Error: Date format not recognized for {due_datetime_str}")
        return None  # Jika format tidak cocok, kembalikan None

    now = datetime.now()
    time_left = due_datetime - now

    if time_left <= timedelta(0):
        return None  # Tidak ada waktu tersisa

    # Hitung jam dan menit tersisa
    total_minutes = int(time_left.total_seconds() / 60)
    hours, minutes = divmod(total_minutes, 60)

    # Format output tanpa leading zero
    if hours > 0:
        return f"{hours} jam {minutes} menit" if minutes > 0 else f"{hours} jam"
    else:
        return f"{minutes} menit"
