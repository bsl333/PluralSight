from pprint import pprint as pp


class Flight:
    def __init__(self, number, aircraft):
        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat_number):
        rows, seat_letters = self._aircraft.seating_plan()
        row_letter = seat_number[-1]
        row_number = seat_number[:-1]

        if row_letter not in seat_letters:
            raise ValueError('{} not a valid seat letter'.format(row_letter))
        try:
            row_number = int(row_number)
        except ValueError:
            raise ValueError('{} not a valid number'.format(seat_number))
        if row_number not in rows:
            raise ValueError('{} not a valid row'.format(row_number))

        return row_number, row_letter

    def allocate_seat(self, seat_number, passenger):
        """

        :param seat_number: ex: 12A, 23F, etc
        :param passenger: string. ex: 'Branden'
        :return: Nothing
        """
        row_number, row_letter = self._parse_seat(seat_number)

        if self._seating[row_number][row_letter] is not None:
            raise ValueError('{} seat occupied'.format(seat_number))

        self._seating[row_number][row_letter] = passenger

    def available_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None)
                   for row in self._seating
                   if row is not None)


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


a = Aircraft('reg', 'Boeing 777', 35, 12)
# print(a.seating_plan())

d = Flight()
f = Flight('on632', a)
print(f.aircraft_model())
f.allocate_seat('3A', 'Branden Lowe')
f.allocate_seat('3C', 'Branden Lowe')
# pp(f._seating)
print(f.available_seats())
