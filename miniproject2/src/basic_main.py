from track import track
import pickle
import sys
import race

def do_the_learning():
    final_car = race.train_car()
    try:
        pickle.dump(final_car, open(sys.argv[1], 'wb'))
    except:
        race.show(final_car)

if __name__ == "__main__":
    do_the_learning()
