def Bresenham(x1, y1, x2, y2):
    tab = []
    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)
    y = y1
    for x in range(x1, x2 + 1):
        tab.append((x, y))
        slope_error_new = slope_error_new + m_new
        if (slope_error_new >= 0):
            y = y + 1
            slope_error_new = slope_error_new - 2 * (x2 - x1)
    return tab
