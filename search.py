
class Search:
    def __init__(self, filename):
        self.filename = filename
        self.countries = []
        self.file = None

        with open(self.filename, "rt") as myfile:
            for myline in myfile:
                self.countries.append(myline.rstrip('\n'))

    def validate(self, soal):
        result = ''
        for count in self.countries:
            if soal in count.lower():                
                result +=  count + '--'
        return result.rstrip('--')               
           
