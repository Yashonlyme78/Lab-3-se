class FlightTable:
    def __init__(self):
        self.data = [
            {'Match Location': 'Mumbai', 'Team 01': 'India', 'Team 02': 'Sri Lanka', 'Timing': 'DAY'},
            {'Match Location': 'Delhi', 'Team 01': 'England', 'Team 02': 'Australia', 'Timing': 'DAY-NIGHT'},
            {'Match Location': 'Chennai', 'Team 01': 'India', 'Team 02': 'South Africa', 'Timing': 'DAY'},
            {'Match Location': 'Indore', 'Team 01': 'England', 'Team 02': 'Sri Lanka', 'Timing': 'DAY-NIGHT'},
            {'Match Location': 'Mohali', 'Team 01': 'Australia', 'Team 02': 'South Africa', 'Timing': 'DAY-NIGHT'},
            {'Match Location': 'Delhi', 'Team 01': 'India', 'Team 02': 'Australia', 'Timing': 'DAY'}
        ]

    def search(self, search_param, value):
        results = []
        for row in self.data:
            if row[search_param] == value:
                results.append(row)
        return results

    def print_results(self, results):
        for row in results:
            print(row)

ft = FlightTable()
search_param = input('Choose search parameter [1. Team, 2. Match Location, 3. Timing]: ')
value = input('Enter parameter: ')

if search_param == "1":
    search_param = "Team 01"
    results = ft.search(search_param, value)
    ft.print_results(results)
    search_param = "Team 02"
    results = ft.search(search_param, value)
    ft.print_results(results)
elif search_param == "2":
    search_param = "Match Location"
    results = ft.search(search_param, value)
    ft.print_results(results)
elif search_param == "3":
    search_param = "Timing"
    results = ft.search(search_param, value)
    ft.print_results(results)
else:
    print("Invalid input")
