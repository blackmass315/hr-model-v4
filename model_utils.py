
def get_hr_score(barrel_rate, exit_velocity, xSLG, sweet_spot, rpi,
                 hr9, hard_hit_pct, fatigue,
                 park_factor, wind_boost, temp_boost):
    # Modified BPS (no /5)
    bps = (
        barrel_rate * 2.0 +
        exit_velocity * 0.5 +
        xSLG * 100 +
        sweet_spot * 0.5 +
        rpi * 100
    )

    pvs = (
        hr9 * 30 +
        hard_hit_pct * 0.5 +
        fatigue * 5
    ) / 3

    final_score = bps * 0.7 + pvs * 0.3
    sleeper = rpi > 0.7 and barrel_rate > 12 and final_score < 85
    return min(round(final_score, 1), 100), sleeper
