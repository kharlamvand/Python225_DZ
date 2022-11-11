class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Расчет заработной платы')
        print('==================================================')
        for employee in employees:
            print(f'Заработная плата: {employee.id} - {employee.name}')
            print(f'- Проверить сумму: {employee.calculate_payroll()}')
            print('')
