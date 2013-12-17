from track import track
import pickle
import sys
import race


if __name__ == "__main__":
    final_car = pickle.load(open(sys.argv[1], 'rb'))
    race.show_race(final_car)
