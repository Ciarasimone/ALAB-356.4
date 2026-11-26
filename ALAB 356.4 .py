# fibonacciiiii
def gen_fibonacci(n):
    #yield  first n numbers of fibonacci
    if n < 0:
        raise ValueError("Count n must be a non-negative integer.")

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    count = 8
    print(f"=== fibonacci sequence (First {count} Numbers) ===")
    for index, value in enumerate(gen_fibonacci(count), start=1):
        print(f"Term {index}: {value}")



# multiplier
def make_multiplier(factor):
    # return closure function that multiplies its input x by factor
    def multiplier(x):
        return x * factor

    return multiplier


if __name__ == "__main__":
    times3 = make_multiplier(3)
    times10 = make_multiplier(10)

    sample_input = 7
    print("=== multiplier closure demo ===")
    print(f"times3({sample_input}) = {times3(sample_input)}")
    print(f"times10({sample_input}) = {times10(sample_input)}")


# diary
def make_multiplier(factor):
    # show a closure function that multiplies its input x by factor
    def multiplier(x):
        return x * factor

    return multiplier


if __name__ == "__main__":
    times3 = make_multiplier(3)
    times10 = make_multiplier(10)

    sample_input = 7
    print("=== multiplier closure demo ===")
    print(f"times3({sample_input}) = {times3(sample_input)}")
    print(f"times10({sample_input}) = {times10(sample_input)}")

# daye and calendar
import calendar
import datetime


def prompt_int(prompt_text, min_val=None, max_val=None):
    # ask for an integer within optional bounds
    while True:
        raw = input(prompt_text).strip()
        try:
            value = int(raw)
            if min_val is not None and value < min_val:
                print(f"enter a number greater than or equal to {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"enter a number less than or equal to {max_val}.")
                continue
            return value
        except ValueError:
            print("invalid input. enter a whole number.")


def main():
    print("=== monthly calendar & today's date utility ===")
    year = prompt_int("Enter a year (e.g., 2026): ", min_val=1)
    month = prompt_int("Enter a month (1-12): ", min_val=1, max_val=12)

    today = datetime.date.today()
    month_grid = calendar.month(year, month)

    print(f"\n--- Calendar for {calendar.month_name[month]} {year} ---")
    print(month_grid.rstrip())

    print("--- today's date ---")
    print(f"Today's date: {today.strftime('%B %d, %Y')}")

    if today.year == year and today.month == month:
        print(f"Match found: Today is {today.strftime('%B %d, %Y')} (Day {today.day} of this displayed month).")
    else:
        print(f"Today ({today.strftime('%B %d, %Y')}) does not fall in {calendar.month_name[month]} {year}.")


if __name__ == "__main__":
    main()
