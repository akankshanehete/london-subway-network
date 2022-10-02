"""
this class reads files and extracts information,
storing the results in a dictionary data structure
for easy access to key value pairs
"""


class Csv_reader:

    # read each line in csv file to a list
    @staticmethod
    def csv_to_list(csv_text):
        rows = []
        lines = csv_text.readlines()
        for line in lines:
            rows.append(line.split(","))
        return rows

    # creates a list, where each item in the list is a dictionary
    # for the values in csv file
    def extract_csv(self, filename):
        csv_file = open(filename, 'r')
        csv_file = self.csv_to_list(csv_file)
        values = []
        first = True
        title = []
        for i in csv_file:
            value = {}
            if first:
                title = i
                # generate dictionary key title for each
                # parameter using first line of csv file
                for j in range(len(title)):
                    title[j] = title[j].strip('"').strip('\n').strip('"')
                first = False
            else:
                # add all values for each parameter
                for j in range(len(title)):
                    value[title[j]] = i[j].strip('"').strip('\n').strip('"')
                values.append(value)
        return values
