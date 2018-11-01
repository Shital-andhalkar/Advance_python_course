from ps_person import Person


class Employee(Person):
        """derived class """
        def __init__(self, eid, fn, ln):
            self.eid = eid
            super().__init__(fn, ln)

        def get_info(self):
            print('emp_id:', self.eid)
            super().get_info()


def main():
    e = Employee('1175191', 'Aditi', 'Vaidya')
    e.get_info()

if __name__ == '__main__':
    main()