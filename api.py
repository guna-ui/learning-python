import requests

def getNumDraws(year):
    base_url = "https://jsonmock.hackerrank.com/api/football_matches"
    total_draws = 0
    page = 1

    while True:
        # Fetch data from the API
        response = requests.get(f"{base_url}?year={year}&page={page}")
        # print(f"Fetching page {page} for year {year}")  # Debugging print statement
        data = response.json()

        # Check if the response contains the expected data
        if "data" not in data:
            print("No data found in the response")
            break

        # Count matches where team1goals == team2goals
        for match in data["data"]:
            if match["team1goals"] == match["team2goals"]:
                total_draws += 1

        # Check if more pages exist
        if page >= data["total_pages"]:
            break

        page += 1

    return total_draws

# Example usage:
year = 2011
draws = getNumDraws(year)
print(f"Total draws in {year}: {draws}")
