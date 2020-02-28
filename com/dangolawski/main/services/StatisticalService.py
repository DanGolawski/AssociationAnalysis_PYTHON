
class StatisticalService:

    def calc_elem_average(self, data):
        elem_counter = 0
        for elem in data:
            elem_counter += len(elem.items)

        return round(elem_counter / len(data))