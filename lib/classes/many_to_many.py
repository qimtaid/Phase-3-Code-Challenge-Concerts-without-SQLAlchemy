# lib/models/many_to_many.py

class Band:
    all_bands = []

    def __init__(self, name, hometown):
        self._name = name
        self._hometown = hometown
        self._concerts = []
        Band.all_bands.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        raise AttributeError("Hometown is immutable")

    def concerts(self):
        return self._concerts

    def venues(self):
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        self._concerts.append(concert)
        return concert

    def all_introductions(self):
        return [f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}" for concert in self._concerts]


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        band.concerts().append(self)
        venue.concerts().append(self)


class Venue:
    all_venues = []

    def __init__(self, name, city):
        self._name = name
        self._city = city
        self._concerts = []
        Venue.all_venues.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string")

    def concerts(self):
        return self._concerts

    def bands(self):
        return list(set(concert.band for concert in self._concerts))

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None
