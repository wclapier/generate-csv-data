import csv
import sys
from faker import Faker

fake = Faker()

def main(argv):

    num_files = int(argv[1])
    num_rows = int(argv[2])
    num_columns = int(argv[3])
    
    for i in range(0, num_files):
        filename = fake.word() + '.csv'
        with open(filename, 'w', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for j in range(0, num_rows):
                writer.writerow(fake.words(num_columns))


if __name__ == "__main__":
    main(sys.argv)
