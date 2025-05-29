import requests
from bs4 import BeautifulSoup


def fetch_entity_info(name):
    """Fetch business entity info from the Texas Comptroller website.

    This uses a simple GET request to the search endpoint.
    The endpoint and parsing logic are placeholders and may need
    adjustment based on the actual site structure.
    """
    search_url = "https://mycpa.cpa.state.tx.us/coa/servlet/cpa.app.coa.PT1"  # Placeholder
    params = {"aname": name}
    response = requests.get(search_url, params=params)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    table = soup.find("table")  # Adjust selector to actual table id/class
    if not table:
        return results

    for row in table.find_all("tr")[1:]:
        cells = [cell.get_text(strip=True) for cell in row.find_all("td")]
        results.append(cells)

    return results


def main(names):
    for name in names:
        data = fetch_entity_info(name)
        print(f"Results for {name}:")
        for entry in data:
            print(entry)
        print()


if __name__ == "__main__":
    sample_names = [
        "Example Business",  # Replace with actual business names
    ]
    main(sample_names)
