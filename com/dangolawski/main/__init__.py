from services.DataService import DataService
from services.StatisticalService import StatisticalService

data_service = DataService()
statistical_service = StatisticalService()


# TODO usunac obiekty z pusta lista produktow jesli takie istnieja
transactions_num, objects = data_service.read_data()
elem_average = statistical_service.calc_elem_average(objects)


