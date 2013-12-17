from track import track
import pickle
import sys
import race


if __name__ == "__main__":
    final_car = pickle.load(open(sys.argv[1], 'rb'))
    first = True
    while first or raw_input() != '0':
        first = False
        race.show_race(final_car)
