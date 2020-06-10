class Z_S_9:
    #Population according to urkstat.gov.ua 1 january 2020 
    region_population_of_khmelnitska = 1254702
    region_population_of_dnipropetrovs = 3176648
    #Area from google in km_2
    square_km_2_khmelnitska = 20629
    square_km_2_dnipropertovs = 31923
    #1 km_2 = 100 ga
    def khmelnitska(self):
        square_ga_khmelnitska = self.square_km_2_khmelnitska * 100
        ga_per_person_h = square_ga_khmelnitska / self.region_population_of_khmelnitska
        print('In Khmelnitsk state every citizen could own: ' + str(ga_per_person_h) + 'ga')
    def dnipropetrovska(self):
        square_ga_dnipropetrovska = self.square_km_2_dnipropertovs * 100
        ga_per_person_d = square_ga_dnipropetrovska / self.region_population_of_dnipropetrovs
        print('In Dnipropetrovsk state every citizen could own: ' + str(ga_per_person_d) + 'ga')

obj1 = Z_S_9()
obj1.khmelnitska()
obj1.dnipropetrovska()
